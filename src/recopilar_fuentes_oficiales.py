import csv
import json
from pathlib import Path
import urllib.request
import urllib.error
import hashlib
from datetime import datetime
from html.parser import HTMLParser
import re
import sys


TARGET_CODES = ["F02", "F03", "F04", "F05", "F06"]
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)
TIMEOUT_SECONDS = 40


class VisibleTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks = []
        self._ignore_depth = 0

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag.lower() in {"script", "style"}:
            self._ignore_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"script", "style"} and self._ignore_depth > 0:
            self._ignore_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._ignore_depth == 0 and data:
            self._chunks.append(data)

    def get_visible_text(self) -> str:
        joined = "\n".join(self._chunks)
        joined = re.sub(r"[\t\r\f\v]+", " ", joined)
        joined = re.sub(r"\n+", "\n", joined)
        joined = re.sub(r" {2,}", " ", joined)
        lines = [line.strip() for line in joined.split("\n")]
        lines = [line for line in lines if line]
        return "\n".join(lines)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\-]+", "_", text, flags=re.UNICODE)
    text = re.sub(r"_+", "_", text)
    return text.strip("_") or "fuente"


def read_inventory(csv_path: Path):
    rows = []
    with csv_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            code = (row.get("codigo_fuente") or "").strip().upper()
            if code in TARGET_CODES:
                rows.append(row)
    return rows


def detect_content_type(content_type_header: str) -> str:
    content_type = (content_type_header or "").lower().strip()
    if content_type.startswith("application/pdf"):
        return "application/pdf"
    if content_type.startswith("text/html"):
        return "text/html"
    return "otros"


def decode_html(raw_bytes: bytes, content_type_header: str) -> str:
    match = re.search(r"charset=([A-Za-z0-9_\-]+)", content_type_header or "", flags=re.IGNORECASE)
    if match:
        encoding = match.group(1).strip()
        try:
            return raw_bytes.decode(encoding, errors="replace")
        except LookupError:
            pass
    return raw_bytes.decode("utf-8", errors="replace")


def save_source_files(code: str, name: str, url: str, content_type_kind: str, raw_bytes: bytes, output_dir: Path, content_type_header: str):
    base_name = f"{code}_{slugify(name)}"

    if content_type_kind == "application/pdf":
        output_file = output_dir / f"{base_name}.pdf"
        output_file.write_bytes(raw_bytes)
        return {
            "archivo_principal": str(output_file),
            "archivo_texto": None,
            "archivo_original": str(output_file),
            "archivo_texto_extraido": None,
        }

    if content_type_kind == "text/html":
        html_file = output_dir / f"{base_name}.html"
        # Preserve exact bytes as delivered by the server for integrity checks.
        html_file.write_bytes(raw_bytes)

        html_text = decode_html(raw_bytes, content_type_header)

        parser = VisibleTextExtractor()
        parser.feed(html_text)
        visible_text = parser.get_visible_text()

        text_file = output_dir / f"{base_name}_texto.txt"
        text_file.write_text(visible_text, encoding="utf-8")

        return {
            "archivo_principal": str(html_file),
            "archivo_texto": str(text_file),
            "archivo_original": str(html_file),
            "archivo_texto_extraido": str(text_file),
        }

    # Extract extension from URL path using regex to avoid non-required imports.
    suffix_match = re.search(r"/[^/?#]+(\.[A-Za-z0-9]{1,10})(?:[?#]|$)", url)
    suffix = suffix_match.group(1).lower() if suffix_match else ""
    if not suffix or len(suffix) > 10:
        suffix = ".bin"
    output_file = output_dir / f"{base_name}{suffix}"
    output_file.write_bytes(raw_bytes)
    return {
        "archivo_principal": str(output_file),
        "archivo_texto": None,
        "archivo_original": str(output_file),
        "archivo_texto_extraido": None,
    }


def download_source(row, output_dir: Path):
    code = (row.get("codigo_fuente") or "").strip().upper()
    name = (row.get("nombre_fuente") or "").strip() or "fuente_sin_nombre"
    original_url = (row.get("url") or "").strip()

    result = {
        "codigo_fuente": code,
        "nombre_fuente": name,
        "url_original": original_url,
        "url_final": None,
        "tipo_contenido": None,
        "tamano_bytes": 0,
        "sha256": None,
        "fecha_hora_descarga": datetime.now().isoformat(timespec="seconds"),
        "estado_descarga": "fallida",
        "mensaje_error": None,
        "archivo_principal": None,
        "archivo_texto": None,
        "archivo_original": None,
        "archivo_texto_extraido": None,
        "tamano_bytes_original": 0,
        "sha256_original": None,
    }

    if not original_url:
        result["mensaje_error"] = "URL vacia en inventario"
        return result

    request = urllib.request.Request(
        original_url,
        headers={"User-Agent": USER_AGENT},
        method="GET",
    )

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            raw_bytes = response.read()
            content_type_header = response.headers.get("Content-Type", "")
            content_type_kind = detect_content_type(content_type_header)
            final_url = response.geturl()

            file_info = save_source_files(
                code=code,
                name=name,
                url=final_url,
                content_type_kind=content_type_kind,
                raw_bytes=raw_bytes,
                output_dir=output_dir,
                content_type_header=content_type_header,
            )

            result["url_final"] = final_url
            result["tipo_contenido"] = content_type_kind
            result["tamano_bytes"] = len(raw_bytes)
            result["sha256"] = hashlib.sha256(raw_bytes).hexdigest()
            result["estado_descarga"] = "exitosa"
            result["archivo_principal"] = file_info["archivo_principal"]
            result["archivo_texto"] = file_info["archivo_texto"]
            result["archivo_original"] = file_info["archivo_original"]
            result["archivo_texto_extraido"] = file_info["archivo_texto_extraido"]
            result["tamano_bytes_original"] = len(raw_bytes)
            result["sha256_original"] = result["sha256"]

    except urllib.error.HTTPError as error:
        result["mensaje_error"] = f"HTTPError {error.code}: {error.reason}"
    except urllib.error.URLError as error:
        result["mensaje_error"] = f"URLError: {error.reason}"
    except TimeoutError:
        result["mensaje_error"] = "TimeoutError: se supero el tiempo maximo de espera"
    except Exception as error:
        result["mensaje_error"] = f"Error inesperado: {error}"

    return result


def build_metadata(results):
    success_count = sum(1 for item in results if item["estado_descarga"] == "exitosa")
    failed_count = sum(1 for item in results if item["estado_descarga"] != "exitosa")
    return {
        "fecha_procesamiento": datetime.now().isoformat(timespec="seconds"),
        "herramienta_utilizada": "src/recopilar_fuentes_oficiales.py",
        "total_fuentes_programadas": len(TARGET_CODES),
        "total_descargas_exitosas": success_count,
        "total_descargas_fallidas": failed_count,
        "resultados_fuentes": results,
        "advertencia_metodologica": (
            "Una descarga exitosa no significa que la fuente haya sido verificada sustantivamente. "
            "El contenido, las cifras, las fechas, las definiciones y el nivel territorial deberán "
            "revisarse y contrastarse con la fuente original antes de utilizarlos en el análisis académico"
        ),
    }


def main() -> int:
    root = project_root()
    inventory_path = root / "datos" / "inventario_fuentes.csv"
    raw_output_dir = root / "documentos" / "fuentes_raw"
    metadata_output_path = root / "resultados" / "recopilacion_fuentes_metadatos.json"

    raw_output_dir.mkdir(parents=True, exist_ok=True)
    metadata_output_path.parent.mkdir(parents=True, exist_ok=True)

    inventory_rows = read_inventory(inventory_path)
    rows_by_code = {
        (row.get("codigo_fuente") or "").strip().upper(): row for row in inventory_rows
    }

    results = []
    for code in TARGET_CODES:
        row = rows_by_code.get(code)
        if row is None:
            results.append(
                {
                    "codigo_fuente": code,
                    "nombre_fuente": None,
                    "url_original": None,
                    "url_final": None,
                    "tipo_contenido": None,
                    "tamano_bytes": 0,
                    "sha256": None,
                    "fecha_hora_descarga": datetime.now().isoformat(timespec="seconds"),
                    "estado_descarga": "fallida",
                    "mensaje_error": "Fuente no encontrada en datos/inventario_fuentes.csv",
                    "archivo_principal": None,
                    "archivo_texto": None,
                    "archivo_original": None,
                    "archivo_texto_extraido": None,
                    "tamano_bytes_original": 0,
                    "sha256_original": None,
                }
            )
            continue

        result = download_source(row, raw_output_dir)
        results.append(result)

    metadata = build_metadata(results)
    metadata_output_path.write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("=" * 50)
    print("RECOPILACIÓN DE FUENTES OFICIALES")
    print("=" * 50)
    for code in TARGET_CODES:
        source_result = next((item for item in results if item["codigo_fuente"] == code), None)
        status = "descarga exitosa" if source_result and source_result["estado_descarga"] == "exitosa" else "descarga fallida"
        print(f"{code}: {status}.")

    print("")
    print(f"Total exitosas: {metadata['total_descargas_exitosas']}")
    print(f"Total fallidas: {metadata['total_descargas_fallidas']}")
    print(f"Archivo de metadatos: {metadata_output_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
