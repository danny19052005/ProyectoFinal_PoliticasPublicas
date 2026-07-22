import json
from pathlib import Path
import hashlib
from datetime import datetime
from html.parser import HTMLParser
import re
import sys


TARGET_CODES = ["F02", "F03", "F04", "F05", "F06"]
ERROR_SIGNAL_PATTERNS = [
    r"\b404\b",
    r"access\s+denied",
    r"forbidden",
    r"page\s+not\s+found",
    r"sitio\s+no\s+disponible",
    r"error\s+interno",
    r"captcha",
    r"verificaci[oó]n\s+de\s+seguridad",
]


class HtmlInspectionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.title_chunks = []
        self.visible_chunks = []
        self.ignored_depth = 0
        self.has_html_tag = False

    def handle_starttag(self, tag, attrs):
        tag_lower = tag.lower()
        if tag_lower == "html":
            self.has_html_tag = True
        if tag_lower == "title":
            self.in_title = True
        if tag_lower in {"script", "style"}:
            self.ignored_depth += 1

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower == "title":
            self.in_title = False
        if tag_lower in {"script", "style"} and self.ignored_depth > 0:
            self.ignored_depth -= 1

    def handle_data(self, data):
        if self.in_title:
            self.title_chunks.append(data)
        if self.ignored_depth == 0:
            self.visible_chunks.append(data)

    def title(self) -> str:
        raw = " ".join(self.title_chunks).strip()
        return normalize_spaces(raw)

    def visible_text(self) -> str:
        return normalize_spaces("\n".join(self.visible_chunks))


def normalize_spaces(text: str) -> str:
    text = re.sub(r"[\t\r\f\v]+", " ", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    lines = [line.strip() for line in text.split("\n")]
    lines = [line for line in lines if line]
    return "\n".join(lines)


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_metadata(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def detect_type_from_extension(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return "application/pdf"
    if suffix in {".html", ".htm"}:
        return "text/html"
    return "otros"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_pdf(path: Path):
    with path.open("rb") as fh:
        header = fh.read(4)
    is_pdf_signature = header == b"%PDF"
    warnings = []
    if not is_pdf_signature:
        warnings.append("La firma binaria inicial no coincide con %PDF")
    return {
        "formato_valido": is_pdf_signature,
        "titulo_o_descripcion": "Archivo PDF (sin extracción de texto en esta etapa)",
        "advertencias": warnings,
        "caracteres_visibles_aprox": None,
        "senales_error_detectadas": [],
        "estructura_html_valida": None,
        "texto_visible_no_vacio": None,
    }


def find_error_signals(text: str):
    found = []
    lowered = text.lower()
    for pattern in ERROR_SIGNAL_PATTERNS:
        if re.search(pattern, lowered, flags=re.IGNORECASE):
            found.append(pattern)
    return found


def validate_html(path: Path):
    html_text = path.read_text(encoding="utf-8", errors="replace")

    parser = HtmlInspectionParser()
    parser.feed(html_text)

    visible_text = parser.visible_text()
    title_text = parser.title()
    structure_valid = parser.has_html_tag or bool(re.search(r"<!doctype\s+html", html_text, flags=re.IGNORECASE))
    visible_count = len(visible_text)
    signal_patterns = find_error_signals(html_text + "\n" + visible_text)

    warnings = []
    if not structure_valid:
        warnings.append("No se detectó etiqueta <html> ni declaración <!DOCTYPE html>")
    if visible_count == 0:
        warnings.append("El texto visible está vacío")
    if signal_patterns:
        warnings.append(
            "Se detectaron expresiones asociadas a posibles bloqueos/errores (revisión humana requerida)"
        )

    formato_valido = structure_valid and visible_count > 0
    description = title_text if title_text else "Página HTML sin título detectable"

    return {
        "formato_valido": formato_valido,
        "titulo_o_descripcion": description,
        "advertencias": warnings,
        "caracteres_visibles_aprox": visible_count,
        "senales_error_detectadas": signal_patterns,
        "estructura_html_valida": structure_valid,
        "texto_visible_no_vacio": visible_count > 0,
    }


def assess_status(exists: bool, formato_valido: bool, warnings_count: int, invalid_reasons_count: int) -> str:
    if not exists:
        return "Archivo no encontrado"
    if invalid_reasons_count > 0:
        return "Archivo posiblemente inválido"
    if warnings_count > 0:
        return "Archivo válido con advertencias"
    if formato_valido:
        return "Archivo técnicamente válido"
    return "Archivo posiblemente inválido"


def validate_source_entry(source_result: dict, seen_paths: dict):
    code = source_result.get("codigo_fuente")
    file_path_raw = source_result.get("archivo_principal")

    base_output = {
        "codigo_fuente": code,
        "archivo": file_path_raw,
        "tipo_registrado": source_result.get("tipo_contenido"),
        "tipo_por_extension": None,
        "archivo_existe": False,
        "tamano_registrado": source_result.get("tamano_bytes"),
        "tamano_actual": None,
        "tamano_coincidente": False,
        "sha256_registrado": source_result.get("sha256"),
        "sha256_actual": None,
        "sha256_coincidente": False,
        "archivo_no_vacio": False,
        "coherencia_tipo_extension": False,
        "archivo_duplicado_entre_fuentes": False,
        "firma_pdf_valida": None,
        "estructura_html_valida": None,
        "texto_visible_no_vacio": None,
        "caracteres_visibles_aprox": None,
        "titulo_o_descripcion": None,
        "advertencias": [],
        "senales_error_detectadas": [],
        "estado_tecnico": None,
    }

    if not file_path_raw:
        base_output["advertencias"].append("No hay archivo registrado en metadatos")
        base_output["estado_tecnico"] = "Archivo no encontrado"
        return base_output

    path = Path(file_path_raw)
    base_output["tipo_por_extension"] = detect_type_from_extension(path)

    if not path.exists():
        base_output["advertencias"].append("El archivo registrado no existe en el sistema de archivos")
        base_output["estado_tecnico"] = "Archivo no encontrado"
        return base_output

    base_output["archivo_existe"] = True

    try:
        stat = path.stat()
        size_now = stat.st_size
        base_output["tamano_actual"] = size_now
        base_output["archivo_no_vacio"] = size_now > 0
        base_output["tamano_coincidente"] = size_now == (base_output["tamano_registrado"] or 0)

        sha_now = file_sha256(path)
        base_output["sha256_actual"] = sha_now
        base_output["sha256_coincidente"] = sha_now == (base_output["sha256_registrado"] or "")

        reg_type = source_result.get("tipo_contenido")
        ext_type = base_output["tipo_por_extension"]
        if reg_type in {"application/pdf", "text/html", "otros"}:
            base_output["coherencia_tipo_extension"] = (
                reg_type == ext_type or reg_type == "otros"
            )
        else:
            base_output["coherencia_tipo_extension"] = False

        resolved = str(path.resolve())
        if resolved in seen_paths:
            base_output["archivo_duplicado_entre_fuentes"] = True
            base_output["advertencias"].append(
                f"Posible duplicado: mismo archivo que {seen_paths[resolved]}"
            )
        else:
            seen_paths[resolved] = code

        if ext_type == "application/pdf":
            pdf_checks = validate_pdf(path)
            base_output["firma_pdf_valida"] = pdf_checks["formato_valido"]
            base_output["titulo_o_descripcion"] = pdf_checks["titulo_o_descripcion"]
            base_output["advertencias"].extend(pdf_checks["advertencias"])

        elif ext_type == "text/html":
            html_checks = validate_html(path)
            base_output["estructura_html_valida"] = html_checks["estructura_html_valida"]
            base_output["texto_visible_no_vacio"] = html_checks["texto_visible_no_vacio"]
            base_output["caracteres_visibles_aprox"] = html_checks["caracteres_visibles_aprox"]
            base_output["titulo_o_descripcion"] = html_checks["titulo_o_descripcion"]
            base_output["senales_error_detectadas"] = html_checks["senales_error_detectadas"]
            base_output["advertencias"].extend(html_checks["advertencias"])

        else:
            base_output["titulo_o_descripcion"] = "Tipo de archivo distinto de PDF/HTML"
            base_output["advertencias"].append(
                "Tipo de archivo no priorizado para validación de formato detallada"
            )

        invalid_reasons = []
        if not base_output["archivo_no_vacio"]:
            invalid_reasons.append("Archivo vacío")
        if not base_output["tamano_coincidente"]:
            invalid_reasons.append("Tamaño no coincide con metadatos")
        if not base_output["sha256_coincidente"]:
            invalid_reasons.append("SHA-256 no coincide con metadatos")
        if not base_output["coherencia_tipo_extension"]:
            invalid_reasons.append("Tipo registrado y extensión no coherentes")
        if ext_type == "application/pdf" and base_output["firma_pdf_valida"] is False:
            invalid_reasons.append("Firma PDF inválida")
        if ext_type == "text/html":
            if base_output["estructura_html_valida"] is False:
                invalid_reasons.append("Estructura HTML inválida")
            if base_output["texto_visible_no_vacio"] is False:
                invalid_reasons.append("Texto visible vacío")

        for reason in invalid_reasons:
            if reason not in base_output["advertencias"]:
                base_output["advertencias"].append(reason)

        status = assess_status(
            exists=True,
            formato_valido=(len(invalid_reasons) == 0),
            warnings_count=len(base_output["advertencias"]),
            invalid_reasons_count=len(invalid_reasons),
        )
        base_output["estado_tecnico"] = status

    except Exception as error:
        base_output["advertencias"].append(f"Error de validación técnica: {error}")
        base_output["estado_tecnico"] = "Archivo posiblemente inválido"

    return base_output


def build_validation_json(results_by_source: list):
    validos = sum(1 for x in results_by_source if x["estado_tecnico"] == "Archivo técnicamente válido")
    con_adv = sum(1 for x in results_by_source if x["estado_tecnico"] == "Archivo válido con advertencias")
    posiblemente_invalidos = sum(
        1 for x in results_by_source if x["estado_tecnico"] == "Archivo posiblemente inválido"
    )
    no_encontrados = sum(1 for x in results_by_source if x["estado_tecnico"] == "Archivo no encontrado")

    return {
        "fecha_validacion": datetime.now().isoformat(timespec="seconds"),
        "herramienta_utilizada": "src/validar_descargas_fuentes.py",
        "total_fuentes_revisadas": len(TARGET_CODES),
        "archivos_validos": validos,
        "archivos_con_advertencias": con_adv,
        "archivos_posiblemente_invalidos": posiblemente_invalidos,
        "archivos_no_encontrados": no_encontrados,
        "resultados_por_fuente": results_by_source,
        "advertencia_metodologica": (
            "La validación técnica comprueba integridad, existencia y formato de los archivos descargados, "
            "pero no confirma todavía la autenticidad institucional, vigencia, pertinencia territorial "
            "ni exactitud sustantiva de su contenido"
        ),
    }


def markdown_bool(value):
    if value is True:
        return "Sí"
    if value is False:
        return "No"
    return "N/A"


def build_markdown_report(results_by_source: list, validation_json: dict, metadata_path: Path):
    lines = []
    lines.append("# Validación técnica de las descargas F02-F06")
    lines.append("")
    lines.append("## 1. Objetivo")
    lines.append("")
    lines.append(
        "Verificar técnicamente la integridad, existencia y coherencia básica de formato de los archivos "
        "descargados para las fuentes F02-F06, sin evaluar todavía su contenido sustantivo."
    )
    lines.append("")
    lines.append("## 2. Archivos y metadatos revisados")
    lines.append("")
    lines.append(f"- Metadatos de entrada: {metadata_path}")
    lines.append("- Carpeta de archivos revisados: documentos/fuentes_raw/")
    lines.append("")
    lines.append("## 3. Criterios de validación")
    lines.append("")
    lines.append("- Existencia de archivo registrado por fuente.")
    lines.append("- Coincidencia de tamaño y hash SHA-256 respecto a metadatos.")
    lines.append("- Verificación de archivo no vacío.")
    lines.append("- Coherencia entre tipo registrado y extensión del archivo.")
    lines.append("- Detección de posibles duplicados entre fuentes.")
    lines.append("- Para PDF: verificación de firma binaria inicial %PDF.")
    lines.append("- Para HTML: estructura HTML, título, texto visible y señales de bloqueo/error.")
    lines.append("")
    lines.append("## 4. Resultados por fuente")
    lines.append("")
    lines.append(
        "| Código | Archivo | Tipo | Tamaño | SHA-256 coincidente | Formato válido | Título o descripción | Advertencias | Estado técnico |"
    )
    lines.append(
        "|---|---|---|---:|---|---|---|---|---|"
    )

    for item in results_by_source:
        code = item.get("codigo_fuente") or "N/A"
        archivo = item.get("archivo") or "No registrado"
        tipo = item.get("tipo_registrado") or "N/A"
        tamano = item.get("tamano_actual")
        tamano_str = str(tamano) if isinstance(tamano, int) else "N/A"
        sha_ok = markdown_bool(item.get("sha256_coincidente"))

        ext_type = item.get("tipo_por_extension")
        formato_valido = "No"
        if ext_type == "application/pdf":
            formato_valido = markdown_bool(item.get("firma_pdf_valida"))
        elif ext_type == "text/html":
            html_ok = item.get("estructura_html_valida") is True and item.get("texto_visible_no_vacio") is True
            formato_valido = markdown_bool(html_ok)
        elif item.get("archivo_existe"):
            formato_valido = "N/A"

        title_or_desc = item.get("titulo_o_descripcion") or "N/A"
        warnings = item.get("advertencias") or []
        warnings_text = "; ".join(warnings) if warnings else "Sin advertencias"
        estado = item.get("estado_tecnico") or "N/A"

        row = (
            f"| {code} | {archivo} | {tipo} | {tamano_str} | {sha_ok} | {formato_valido} | "
            f"{title_or_desc} | {warnings_text} | {estado} |"
        )
        lines.append(row)

    lines.append("")
    lines.append("## 5. Posibles errores o bloqueos detectados")
    lines.append("")

    any_signals = False
    for item in results_by_source:
        code = item.get("codigo_fuente") or "N/A"
        signals = item.get("senales_error_detectadas") or []
        if signals:
            any_signals = True
            unique_signals = sorted(set(signals))
            lines.append(f"- {code}: {', '.join(unique_signals)}")

    if not any_signals:
        lines.append("- No se detectaron señales textuales de bloqueo/error según los patrones configurados.")

    lines.append("")
    lines.append("## 6. Limitaciones")
    lines.append("")
    lines.append("- Esta validación no confirma autenticidad institucional, vigencia ni pertinencia territorial.")
    lines.append("- La presencia de palabras asociadas a error/bloqueo se reporta como advertencia y requiere revisión humana.")
    lines.append("- No se realizó análisis sustantivo de política pública ni extracción de estadísticas.")
    lines.append("")
    lines.append("## 7. Estado de la validación")
    lines.append("")
    lines.append(
        "La validación técnica quedó registrada para F02-F06. "
        "La validación sustantiva y la revisión humana todavía estarán pendientes."
    )
    lines.append("")
    lines.append("### Resumen")
    lines.append("")
    lines.append(f"- Archivos válidos: {validation_json['archivos_validos']}")
    lines.append(f"- Archivos con advertencias: {validation_json['archivos_con_advertencias']}")
    lines.append(f"- Archivos posiblemente inválidos: {validation_json['archivos_posiblemente_invalidos']}")
    lines.append(f"- Archivos no encontrados: {validation_json['archivos_no_encontrados']}")

    return "\n".join(lines)


def print_terminal_summary(results_by_source: list, validation_json: dict):
    print("=" * 50)
    print("VALIDACIÓN TÉCNICA DE FUENTES")
    print("=" * 50)

    indexed = {item.get("codigo_fuente"): item for item in results_by_source}
    for code in TARGET_CODES:
        status = indexed.get(code, {}).get("estado_tecnico", "Sin resultado")
        print(f"{code}: {status}")

    print("")
    print(f"Archivos válidos: {validation_json['archivos_validos']}")
    print(f"Archivos con advertencias: {validation_json['archivos_con_advertencias']}")
    print(f"Archivos posiblemente inválidos: {validation_json['archivos_posiblemente_invalidos']}")
    print(f"Archivos no encontrados: {validation_json['archivos_no_encontrados']}")


def main() -> int:
    root = project_root()
    metadata_input = root / "resultados" / "recopilacion_fuentes_metadatos.json"
    validation_json_output = root / "resultados" / "validacion_descargas_fuentes.json"
    validation_md_output = root / "documentos" / "validacion_tecnica_descargas_F02_F06.md"

    validation_json_output.parent.mkdir(parents=True, exist_ok=True)
    validation_md_output.parent.mkdir(parents=True, exist_ok=True)

    if not metadata_input.exists():
        print("No se encontró el archivo de metadatos de recopilación:")
        print(metadata_input)
        return 1

    try:
        metadata = load_metadata(metadata_input)
    except Exception as error:
        print(f"Error al leer metadatos: {error}")
        return 1

    results_input = metadata.get("resultados_fuentes", [])
    by_code = {
        (entry.get("codigo_fuente") or "").strip().upper(): entry
        for entry in results_input
        if isinstance(entry, dict)
    }

    results_by_source = []
    seen_paths = {}
    for code in TARGET_CODES:
        source_result = by_code.get(code)
        if source_result is None:
            results_by_source.append(
                {
                    "codigo_fuente": code,
                    "archivo": None,
                    "tipo_registrado": None,
                    "tipo_por_extension": None,
                    "archivo_existe": False,
                    "tamano_registrado": None,
                    "tamano_actual": None,
                    "tamano_coincidente": False,
                    "sha256_registrado": None,
                    "sha256_actual": None,
                    "sha256_coincidente": False,
                    "archivo_no_vacio": False,
                    "coherencia_tipo_extension": False,
                    "archivo_duplicado_entre_fuentes": False,
                    "firma_pdf_valida": None,
                    "estructura_html_valida": None,
                    "texto_visible_no_vacio": None,
                    "caracteres_visibles_aprox": None,
                    "titulo_o_descripcion": "Fuente no encontrada en metadatos",
                    "advertencias": ["Fuente no encontrada en resultados de recopilación"],
                    "senales_error_detectadas": [],
                    "estado_tecnico": "Archivo no encontrado",
                }
            )
            continue

        result = validate_source_entry(source_result, seen_paths)
        results_by_source.append(result)

    validation_json = build_validation_json(results_by_source)
    validation_json_output.write_text(
        json.dumps(validation_json, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    validation_md = build_markdown_report(results_by_source, validation_json, metadata_input)
    validation_md_output.write_text(validation_md, encoding="utf-8")

    print_terminal_summary(results_by_source, validation_json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
