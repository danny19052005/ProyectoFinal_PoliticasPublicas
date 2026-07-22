import json
from pathlib import Path
from datetime import datetime
import re
import sys

from pypdf import PdfReader


TARGET_CODES = ["F02", "F03", "F04", "F05", "F06"]
METHODOLOGICAL_WARNING = (
    "La preparación de textos facilita la revisión documental, pero no sustituye la lectura de la fuente original. "
    "Toda cifra, fecha, definición, ámbito territorial y afirmación institucional deberá contrastarse antes "
    "de utilizarse en el análisis académico"
)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalize_text_content(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = re.sub(r"[ \t]{2,}", " ", normalized)
    normalized = re.sub(r"[ \t]+\n", "\n", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip() + "\n"


def source_map_by_code(items):
    by_code = {}
    if isinstance(items, list):
        for item in items:
            if isinstance(item, dict):
                code = (item.get("codigo_fuente") or "").strip().upper()
                if code in TARGET_CODES:
                    by_code[code] = item
    return by_code


def find_file_by_code(raw_dir: Path, code: str, mode: str):
    candidates = []

    for path in raw_dir.iterdir():
        if not path.is_file():
            continue
        if not path.name.upper().startswith(f"{code}_"):
            continue

        lower_name = path.name.lower()
        if mode == "html_text" and lower_name.endswith("_texto.txt"):
            candidates.append(path)
        elif mode == "html" and lower_name.endswith(".html"):
            candidates.append(path)
        elif mode == "pdf" and lower_name.endswith(".pdf"):
            candidates.append(path)

    if not candidates:
        return None

    candidates.sort(key=lambda p: p.name.lower())
    return candidates[0]


def format_header(
    code: str,
    source_name: str,
    institution: str,
    url_original: str,
    archivo_original: str,
    tipo_contenido: str,
    estado_validacion: str,
) -> str:
    lines = [
        f"Código de la fuente: {code}",
        f"Nombre de la fuente: {source_name}",
        f"Institución: {institution}",
        f"URL original: {url_original}",
        f"Archivo original utilizado: {archivo_original}",
        f"Tipo de contenido: {tipo_contenido}",
        f"Estado de validación técnica: {estado_validacion}",
        "Advertencia: Este texto preparado facilita la revisión documental y debe contrastarse con la fuente original antes del análisis académico.",
        "",
        "==================================================",
        "TEXTO PREPARADO",
        "==================================================",
        "",
    ]
    return "\n".join(lines)


def process_html_source(code: str, raw_dir: Path, source_meta: dict, validation_meta: dict, output_dir: Path):
    result = {
        "codigo_fuente": code,
        "archivo_original": None,
        "archivo_texto_generado": None,
        "tipo_contenido": source_meta.get("tipo_contenido") or "text/html",
        "caracteres_extraidos": 0,
        "total_paginas": None,
        "paginas_con_texto": None,
        "paginas_sin_texto": None,
        "estado_procesamiento": "con_error",
        "mensaje_error": None,
    }

    try:
        text_source_path = find_file_by_code(raw_dir, code, "html_text")
        if text_source_path is None:
            raise FileNotFoundError(f"No se encontró archivo _texto.txt para {code}")

        original_file = source_meta.get("archivo_original") or source_meta.get("archivo_principal")
        if not original_file:
            html_original = find_file_by_code(raw_dir, code, "html")
            original_file = str(html_original) if html_original else "No disponible"

        source_name = source_meta.get("nombre_fuente") or "No disponible en metadatos"
        institution = source_meta.get("institucion") or "No disponible en metadatos"
        url_original = source_meta.get("url_original") or "No disponible en metadatos"
        tipo_contenido = source_meta.get("tipo_contenido") or "text/html"
        estado_validacion = validation_meta.get("estado_tecnico") or "No disponible en metadatos"

        raw_text = text_source_path.read_text(encoding="utf-8", errors="replace")
        prepared_text = normalize_text_content(raw_text)

        header = format_header(
            code=code,
            source_name=source_name,
            institution=institution,
            url_original=url_original,
            archivo_original=original_file,
            tipo_contenido=tipo_contenido,
            estado_validacion=estado_validacion,
        )

        output_path = output_dir / f"{code}_texto_preparado.txt"
        output_path.write_text(header + prepared_text, encoding="utf-8")

        result["archivo_original"] = original_file
        result["archivo_texto_generado"] = str(output_path)
        result["caracteres_extraidos"] = len(prepared_text)
        result["estado_procesamiento"] = "exitosa"

    except Exception as error:
        result["mensaje_error"] = str(error)

    return result


def process_pdf_source(code: str, raw_dir: Path, source_meta: dict, validation_meta: dict, output_dir: Path):
    result = {
        "codigo_fuente": code,
        "archivo_original": None,
        "archivo_texto_generado": None,
        "tipo_contenido": source_meta.get("tipo_contenido") or "application/pdf",
        "caracteres_extraidos": 0,
        "total_paginas": None,
        "paginas_con_texto": None,
        "paginas_sin_texto": None,
        "estado_procesamiento": "con_error",
        "mensaje_error": None,
    }

    try:
        pdf_path = find_file_by_code(raw_dir, code, "pdf")
        if pdf_path is None:
            raise FileNotFoundError(f"No se encontró PDF para {code}")

        source_name = source_meta.get("nombre_fuente") or "No disponible en metadatos"
        institution = source_meta.get("institucion") or "No disponible en metadatos"
        url_original = source_meta.get("url_original") or "No disponible en metadatos"
        tipo_contenido = source_meta.get("tipo_contenido") or "application/pdf"
        estado_validacion = validation_meta.get("estado_tecnico") or "No disponible en metadatos"

        header = format_header(
            code=code,
            source_name=source_name,
            institution=institution,
            url_original=url_original,
            archivo_original=str(pdf_path),
            tipo_contenido=tipo_contenido,
            estado_validacion=estado_validacion,
        )

        reader = PdfReader(str(pdf_path))
        total_paginas = len(reader.pages)
        paginas_con_texto = 0
        paginas_sin_texto = 0

        text_parts = [header]
        for page_index, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text() or ""
            has_text = bool(page_text.strip())

            if has_text:
                paginas_con_texto += 1
            else:
                paginas_sin_texto += 1

            text_parts.append(f"===== PÁGINA {page_index} =====")
            if has_text:
                text_parts.append(page_text)
            else:
                text_parts.append("[Sin texto extraíble en esta página]")
            text_parts.append("")

        prepared_text = "\n".join(text_parts).strip() + "\n"

        output_path = output_dir / f"{code}_texto_preparado.txt"
        output_path.write_text(prepared_text, encoding="utf-8")

        result["archivo_original"] = str(pdf_path)
        result["archivo_texto_generado"] = str(output_path)
        result["caracteres_extraidos"] = len(prepared_text)
        result["total_paginas"] = total_paginas
        result["paginas_con_texto"] = paginas_con_texto
        result["paginas_sin_texto"] = paginas_sin_texto
        result["estado_procesamiento"] = "exitosa"

    except Exception as error:
        result["mensaje_error"] = str(error)

    return result


def print_summary(results_by_source: list, success_count: int, error_count: int, output_dir: Path, metadata_output: Path):
    print("=" * 50)
    print("PREPARACIÓN DE TEXTOS F02-F06")
    print("=" * 50)

    status_by_code = {item.get("codigo_fuente"): item.get("estado_procesamiento") for item in results_by_source}
    for code in TARGET_CODES:
        print(f"{code}: {status_by_code.get(code, 'con_error')}")

    print("")
    print(f"Fuentes procesadas correctamente: {success_count}")
    print(f"Fuentes con error: {error_count}")
    print(f"Directorio de textos: {output_dir}")
    print(f"Archivo de metadatos: {metadata_output}")


def main() -> int:
    root = project_root()
    raw_dir = root / "documentos" / "fuentes_raw"
    recopilacion_path = root / "resultados" / "recopilacion_fuentes_metadatos.json"
    validacion_path = root / "resultados" / "validacion_descargas_fuentes.json"
    output_dir = root / "resultados" / "fuentes_texto"
    preparation_metadata_path = root / "resultados" / "preparacion_textos_F02_F06.json"

    output_dir.mkdir(parents=True, exist_ok=True)
    preparation_metadata_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        recopilacion_data = load_json(recopilacion_path)
    except Exception as error:
        print(f"No se pudo leer {recopilacion_path}: {error}")
        return 1

    try:
        validacion_data = load_json(validacion_path)
    except Exception as error:
        print(f"No se pudo leer {validacion_path}: {error}")
        return 1

    source_meta_by_code = source_map_by_code(recopilacion_data.get("resultados_fuentes", []))
    validation_by_code = source_map_by_code(validacion_data.get("resultados_por_fuente", []))

    results_by_source = []
    for code in TARGET_CODES:
        source_meta = source_meta_by_code.get(code, {"codigo_fuente": code})
        validation_meta = validation_by_code.get(code, {"codigo_fuente": code})

        if code == "F03":
            source_result = process_pdf_source(code, raw_dir, source_meta, validation_meta, output_dir)
        else:
            source_result = process_html_source(code, raw_dir, source_meta, validation_meta, output_dir)

        results_by_source.append(source_result)

    success_count = sum(1 for item in results_by_source if item.get("estado_procesamiento") == "exitosa")
    error_count = sum(1 for item in results_by_source if item.get("estado_procesamiento") != "exitosa")

    preparation_metadata = {
        "fecha_procesamiento": datetime.now().isoformat(timespec="seconds"),
        "herramienta_utilizada": "src/preparar_textos_fuentes_F02_F06.py",
        "total_fuentes_procesadas": len(TARGET_CODES),
        "total_fuentes_exitosas": success_count,
        "total_fuentes_con_error": error_count,
        "resultados_por_fuente": results_by_source,
        "advertencia_metodologica": METHODOLOGICAL_WARNING,
    }

    preparation_metadata_path.write_text(
        json.dumps(preparation_metadata, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print_summary(results_by_source, success_count, error_count, output_dir, preparation_metadata_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
