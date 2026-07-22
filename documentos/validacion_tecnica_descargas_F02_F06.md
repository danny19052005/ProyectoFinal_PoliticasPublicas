# Validación técnica de las descargas F02-F06

## 1. Objetivo

Verificar técnicamente la integridad, existencia y coherencia básica de formato de los archivos descargados para las fuentes F02-F06, sin evaluar todavía su contenido sustantivo.

## 2. Archivos y metadatos revisados

- Metadatos de entrada: C:\Users\monse\OneDrive\Desktop\ProyectoFinal_PoliticasPublicas\resultados\recopilacion_fuentes_metadatos.json
- Carpeta de archivos revisados: documentos/fuentes_raw/

## 3. Criterios de validación

- Existencia de archivo registrado por fuente.
- Coincidencia de tamaño y hash SHA-256 respecto a metadatos.
- Verificación de archivo no vacío.
- Coherencia entre tipo registrado y extensión del archivo.
- Detección de posibles duplicados entre fuentes.
- Para PDF: verificación de firma binaria inicial %PDF.
- Para HTML: estructura HTML, título, texto visible y señales de bloqueo/error.

## 4. Resultados por fuente

| Código | Archivo | Tipo | Tamaño | SHA-256 coincidente | Formato válido | Título o descripción | Advertencias | Estado técnico |
|---|---|---|---:|---|---|---|---|---|
| F02 | C:\Users\monse\OneDrive\Desktop\ProyectoFinal_PoliticasPublicas\documentos\fuentes_raw\F02_seguimiento_al_plan_metropolitano_de_seguridad_y_convivencia_ciudadana_2023-2027.html | text/html | 196552 | Sí | Sí | Seguimiento al Plan Metropolitano de Seguridad y Convivencia Ciudadana 2023-2027 – Observatorio Seguridad Accessibility Tools Increase Text Decrease Text Grayscale High Contrast Negative Contrast Light Background Links Underline Readable Font Reset | Se detectaron expresiones asociadas a posibles bloqueos/errores (revisión humana requerida) | Archivo válido con advertencias |
| F03 | C:\Users\monse\OneDrive\Desktop\ProyectoFinal_PoliticasPublicas\documentos\fuentes_raw\F03_resolución_admq_008-2024.pdf | application/pdf | 606788 | Sí | Sí | Archivo PDF (sin extracción de texto en esta etapa) | Sin advertencias | Archivo técnicamente válido |
| F04 | C:\Users\monse\OneDrive\Desktop\ProyectoFinal_PoliticasPublicas\documentos\fuentes_raw\F04_justicia_y_crimen.html | text/html | 58279 | Sí | Sí | Justicia y crimen | | Sin advertencias | Archivo técnicamente válido |
| F05 | C:\Users\monse\OneDrive\Desktop\ProyectoFinal_PoliticasPublicas\documentos\fuentes_raw\F05_encuesta_de_victimización_y_percepción_de_inseguridad_2011.html | text/html | 113174 | Sí | Sí | Ecuador - Encuesta de Victimización y Percepción de Inseguridad 2011 | Sin advertencias | Archivo técnicamente válido |
| F06 | C:\Users\monse\OneDrive\Desktop\ProyectoFinal_PoliticasPublicas\documentos\fuentes_raw\F06_estadísticas_de_emergencias_coordinadas_en_2024.html | text/html | 73076 | Sí | Sí | El ECU 911 coordinó la atención de más de 3 millones de emergencias en 2024 – Servicio Integrado de Seguridad ECU 911 | Sin advertencias | Archivo técnicamente válido |

## 5. Posibles errores o bloqueos detectados

- F02: \b404\b

## 6. Limitaciones

- Esta validación no confirma autenticidad institucional, vigencia ni pertinencia territorial.
- La presencia de palabras asociadas a error/bloqueo se reporta como advertencia y requiere revisión humana.
- No se realizó análisis sustantivo de política pública ni extracción de estadísticas.

## 7. Estado de la validación

La validación técnica quedó registrada para F02-F06. La validación sustantiva y la revisión humana todavía estarán pendientes.

### Resumen

- Archivos válidos: 4
- Archivos con advertencias: 1
- Archivos posiblemente inválidos: 0
- Archivos no encontrados: 0