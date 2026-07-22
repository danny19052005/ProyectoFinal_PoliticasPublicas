# Registro de decisiones del sistema multiagéntico

## Propósito

Este documento tiene por objeto registrar de manera formal las decisiones adoptadas durante el desarrollo del proyecto académico sobre la implementación de la política pública de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito. Su función es servir como evidencia técnica y académica del proceso de análisis, coordinación y validación entre los agentes del sistema.

## Importancia de registrar las decisiones

En un sistema multiagéntico aplicado al análisis de políticas públicas, el registro de decisiones es esencial porque permite:

- asegurar la trazabilidad del proceso de investigación;
- documentar los acuerdos, criterios y cambios de enfoque;
- facilitar la revisión metodológica y la validación académica;
- mejorar la transparencia en la toma de decisiones;
- fortalecer la confiabilidad de los hallazgos y de los productos generados.

Este registro contribuye a demostrar que el proyecto fue desarrollado de forma organizada, crítica y sustentada en evidencia.

## Tabla de registro

| Fecha | Agente responsable | Tarea realizada | Resultado obtenido | Observaciones | Decisión | Validación humana |
|---|---|---|---|---|---|---|
| 2026-07-21 | Agente Coordinador | Definición de la estructura general del proyecto | Se estableció la arquitectura base del repositorio y los módulos de trabajo | Se priorizó una organización profesional y escalable | Aceptada | Pendiente |
| 2026-07-21 | Agente Coordinador | Diseño de la arquitectura multiagéntica | Se definieron los roles principales y subagentes del sistema | La distribución de funciones fue alineada con los objetivos del análisis | Aceptada | Pendiente |
| 2026-07-21 | Agente Especialista en Políticas Públicas | Definición del contexto del problema público | Se estableció el marco conceptual del caso de estudio | Se identificó la relevancia del análisis institucional y normativo | Aceptada | Pendiente |
| 2026-07-21 | Agente de Datos y Metodología | Organización del enfoque metodológico inicial | Se definieron los insumos para análisis y tabulación de información | Se priorizó la claridad y reproducibilidad metodológica | Aceptada | Pendiente |
| 2026-07-21 | Agente Programador y Visualización | Estructuración de la base para dashboard y visualizaciones | Se preparó la base técnica para futuras gráficas y productos visuales | Se estableció la ruta inicial de implementación técnica | Aceptada | Pendiente |
| 2026-07-21 | Subagente Verificador de fuentes y normativa | Revisión inicial de fuentes y referencias | Se identificó la necesidad de priorizar documentos y cifras oficiales | Se recomienda mantener una política de validación documental | Aceptada | Pendiente |
| 2026-07-21 | Subagente Revisor crítico | Revisión inicial de coherencia metodológica y técnica | Se estableció la necesidad de validar resultados antes de aceptarlos | Se recomienda incorporar revisiones previas a la consolidación final | Aceptada | Pendiente |
| 2026-07-21 | Agente Coordinador | Creación y corrección de .gitignore | Archivo creado con 11 grupos de exclusiones comentados; posteriormente se corrigió eliminando package-lock.json y yarn.lock para mejorar reproducibilidad | Se priorizó la seguridad de publicación y reproducibilidad del dashboard | Aceptada | Completada por el estudiante |
| 2026-07-21 | Agente Especialista en Políticas Públicas | Creación de README.md en carpetas principales | Se crearon 6 archivos README.md en datos/, documentos/, dashboard/, prompts/, resultados/ y src/ | Cada archivo documenta propósito, tipos de contenido y requisitos de documentación | Aceptada | Completada por el estudiante |
| 2026-07-21 | Agente Especialista en Políticas Públicas | Actualización del README.md principal | Se reescribió README con 16 secciones académicas: título, descripción, modalidad, problema, pregunta central, objetivos, instituciones, fuentes, indicadores, metodología, arquitectura, estructura, ejecución, estado actual, enlaces y autoría | Documento académico profesional completo; se respetó la prohibición de inventar cifras, enlaces o fechas | Aceptada | Completada por el estudiante |
| 2026-07-21 | Agente de Datos y Metodología | Elaboración del diseño metodológico completo | Se creó documentos/diseno_metodologico.md con 14 secciones: modalidad, unidad de análisis, delimitaciones, objetivos, enfoque, dimensiones (11), matriz metodológica, criterios de interpretación, limitaciones y procedimiento de validación | Documento riguroso de 11 dimensiones de análisis; se clarificó la prohibición de atribuir causalidad; se documentaron limitaciones metodológicas previstas | Aceptada | Completada por el estudiante |
| 2026-07-21 | Agente de Datos y Metodología | Creación de matriz de fuentes oficiales e inventario | Se crearon dos archivos: matriz_fuentes_oficiales.md (tabla + 5 secciones) e inventario_fuentes.csv (6 fuentes F01-F06) | Se documentaron 6 fuentes con URLs completas; F05 marcada como antecedente histórico 2011; ninguna fuente marcada como verificada | Aceptada | Completada por el estudiante |
| 2026-07-21 | Subagente Revisor Crítico | Validación estructural de archivos de fuentes | Verificación de 7 criterios de calidad: estructura CSV, 6 registros, integridad de campos, URLs completas, advertencia F05, estado de verificación, consistencia entre archivos | Se confirmó estructura correcta, 11 columnas en orden, códigos F01-F06 consistentes, URLs íntegras, F05 con advertencia clara, ninguna fuente verificada completamente | Aceptada | Completada por el estudiante |
| 2026-07-21 | Subagente Verificador de Fuentes | Extracción y revisión estructural preliminar de la fuente F01 | PDF procesado; texto y metadatos generados; índice de verificación elaborado con 8 secciones: identificación, resultado de extracción, índice estructural, mapa de páginas relevantes, fragmentos para revisión, hallazgos documentales, limitaciones y estado | 176 páginas procesadas: 163 con texto extraíble y 13 sin texto. Índice de verificación identifica estructura del Plan, temas relevantes, limitaciones de extracción automática. Esta actividad no constituye verificación completa del contenido ni de las cifras del documento. | Aceptada | El estudiante ejecutó el script de extracción y comprobó el resultado mostrado en terminal |
| 2026-07-21 | Subagente Revisor Crítico | Auditoría de evidencia de los hallazgos preliminares de F01 | Validación de afirmaciones cuantitativas, índice estructural y mapa de páginas. Documento de validación creado: validacion_critica_hallazgos_F01.md. Índice preliminar corregido en 3 ubicaciones. Afirmaciones conservadas tienen respaldo en texto extraído. | Errores identificados y corregidos: página inicial Diagnóstico (56→57), página inicial Planeación (128→129), página inicial Bibliografía (154→155). Afirmaciones cuantitativas confirmadas parcialmente: literal en Página 17 pero no validables plenamente desde Tabla 25 y Figura 74 (extracción incompleta). Riesgos documentados: tablas complejas no completamente extraídas, figuras parcialmente capturadas. | Aceptada | Pendiente de contraste visual del estudiante con el PDF original |
| 2026-07-21 | Estudiante con apoyo del Subagente Verificador de Fuentes | Contraste visual de afirmaciones estructurales de la fuente F01 con el PDF original | Se verificaron visualmente todas las afirmaciones cuantitativas principales: 4 ejes, 5 objetivos, 8 políticas, 15 programas, 27 proyectos. Documentos actualizados: validacion_critica_hallazgos_F01.md (nueva sección 9) e indice_verificacion_plan_F01.md (referencias a páginas del PDF verificadas). | Página 17 (visor del PDF): contiene el resumen de cantidades (4 ejes, 5 objetivos, 8 políticas, 15 programas, 27 proyectos). Figura 74 (página 140 del visor del PDF): confirma visualmente 4 ejes y 5 objetivos. Tabla 25 (páginas 146-148 del visor del PDF): confirma visualmente 8 políticas, 15 programas, 27 proyectos. Aclaración: página 140 en visor (anteriormente referida como 139 en marcador de extracción). | Aceptada | Realizada directamente por el estudiante mediante revisión del PDF original |
| 2026-07-21 | Agente Especialista en Políticas Públicas con apoyo del Subagente Verificador de Fuentes | Revisión sustantiva preliminar de las fuentes F02-F06 | Clasificación de pertinencia, alcance territorial, utilidad metodológica y limitaciones | Diferenciar fuentes normativas, estadísticas, de seguimiento, percepción y emergencias | Aceptada | Pendiente de contraste final del estudiante con las fuentes originales |
| 2026-07-22 | Agente Especialista en Políticas Públicas con revisión del Agente de Datos y los subagentes verificador y crítico | Análisis documental profundo de la evidencia de implementación contenida en F02 | Matriz de evidencia, clasificación de actividades, productos, coordinación, cobertura, indicadores y limitaciones | Distinguir planificación, ejecución, productos y resultados; no inferir incumplimiento por ausencia de información | Aceptada | Pendiente de revisión del estudiante y contraste final con el portal original |
| 2026-07-22 | Agente Especialista en Políticas Públicas con revisión del Subagente Verificador y del Subagente Revisor Crítico | Análisis institucional y normativo de la Resolución ADMQ 008-2024 | Identificación de fundamentos jurídicos, responsabilidades, disposiciones de implementación, coordinación y mecanismos de seguimiento | Distinguir obligación normativa de evidencia de cumplimiento efectivo | Aceptada | Pendiente de contraste del estudiante con el PDF original |
| 2026-07-22 | Agente de Datos y Metodología con revisión del Subagente Verificador de Fuentes y del Subagente Revisor Crítico | Análisis estadístico y contextual del portal Justicia y crimen del INEC | Identificación de productos estadísticos, periodos, niveles territoriales, conceptos y limitaciones para el análisis de Quito | Evitar presentar datos nacionales como datos del Distrito Metropolitano de Quito y diferenciar registros administrativos, encuestas y emergencias | Aceptada | Pendiente de revisión del estudiante y descarga de bases específicas cuando corresponda |
| 2026-07-22 | Agente de Datos y Metodología con revisión del Subagente Verificador de Fuentes y del Subagente Revisor Crítico | Análisis histórico y metodológico de la Encuesta de Victimización y Percepción de Inseguridad 2011 | Identificación de conceptos, variables, diseño metodológico, alcance territorial, utilidad histórica y limitaciones | La fuente corresponde a 2011 y no representa la percepción actual de inseguridad en Quito | Aceptada únicamente como antecedente histórico o metodológico | Pendiente de revisión del estudiante y contraste con documentación y microdatos originales |
| 2026-07-22 | Agente de Datos y Metodología con revisión del Agente Especialista en Políticas Públicas y de los subagentes verificador y crítico | análisis operativo y contextual de las emergencias coordinadas por el ECU 911 en 2024. | identificación de conceptos operativos, cifras, categorías, instituciones, coordinación, cobertura y limitaciones. | diferenciar emergencias, llamadas, incidentes y delitos; registrar Quito como localidad de la fuente y evitar equivalencia automática con el DMQ o con delitos. | Aceptada | pendiente de revisión del estudiante y contraste final con la publicación original. |
| 2026-07-22 | Agente Coordinador con integración del Agente Especialista, Agente de Datos y revisión de los subagentes verificador y crítico | integración y triangulación de la evidencia de las fuentes F01-F06 | síntesis general, matriz integrada por dimensiones y resumen estructurado para el dashboard | diferenciar estructura planificada, obligaciones normativas, seguimiento, contexto estadístico, antecedentes de percepción y emergencias operativas | Aceptada | pendiente de revisión integral del estudiante antes de incorporar los resultados al informe y al dashboard |
| 2026-07-22 | Subagente Revisor Crítico con apoyo del Subagente Verificador de Fuentes | auditoría final de consistencia y trazabilidad de la síntesis integrada F01-F06 | revisión de dimensiones, hallazgos, estados de evidencia, niveles de confianza y consistencia entre Markdown, CSV y JSON | corregir contradicciones y evitar sobreinterpretaciones antes de utilizar la síntesis en el dashboard y el informe | Aceptada únicamente si la síntesis final conserva las limitaciones metodológicas | pendiente de revisión integral del estudiante |
| 2026-07-22 | Agente de Programación y Visualización con revisión del Agente de Datos y de los subagentes verificador y crítico | actualización del dashboard con la síntesis integrada y auditada F01-F06 | dashboard dinámico, archivo de datos local, filtros, visualizaciones y configuración estática para Vercel | mantener advertencias metodológicas y no representar estados cualitativos como porcentajes | Aceptada | pendiente de prueba local y revisión visual del estudiante |
| 2026-07-22 | Subagente Revisor Crítico con validación visual del estudiante | corrección de duplicación entre los hallazgos HI-08 y HI-09 del dashboard | hallazgos diferenciados y archivos JSON sincronizados | la duplicación fue detectada durante la prueba local del dashboard | Aceptada | el estudiante identificó visualmente la repetición en el dashboard |
| 2026-07-22 | Agente de Programación y Visualización con validación del estudiante | despliegue y comprobación del dashboard en Vercel | dashboard publicado mediante un enlace público y conectado al repositorio de GitHub | el dashboard utiliza la síntesis integrada y auditada F01-F06 | Aceptada | el estudiante abrió el dashboard desplegado y copió el enlace público |
| 2026-07-22 | Agente Coordinador con participación de los agentes especialistas y los subagentes verificador y crítico | elaboración del informe académico integral con formato institucional de referencia | borrador académico preparado para una extensión de 20 a 25 páginas y conversión posterior a PDF institucional | se incorporaron datos institucionales, docente, portada, enlaces y especificaciones visuales | Pendiente de auditoría final | pendiente de revisión del estudiante, comprobación de extensión y conversión a PDF |
| 2026-07-22 | Agente Coordinador con validación final del estudiante | cierre de entregables y registro del video, informe PDF y documento editable | todos los entregables principales quedaron disponibles y registrados | se verificaron repositorio, dashboard, video e informe final | Aceptada | realizada por el estudiante antes de la entrega |

**Aclaración:** Esta validación visual confirma cantidades y estructura planificada del Plan, pero no constituye evidencia de ejecución, cobertura, cumplimiento de metas o resultados alcanzados. El documento es un Plan de PLANIFICACIÓN ESTRATÉGICA, no un informe de implementación.

**Aclaración:** Esta revisión documental preliminar no equivale a validación definitiva de todas las cifras ni permite concluir éxito, fracaso o impacto causal de la política.

**Aclaración:** El análisis de F02 permite identificar evidencia documental de seguimiento, pero no demuestra por sí solo impacto causal ni permite atribuir todos los cambios observados a la política.

**Aclaración:** La existencia de una disposición normativa confirma una obligación o competencia formal, pero no demuestra automáticamente que haya sido ejecutada, financiada o cumplida.

**Aclaración:** Las estadísticas de justicia y crimen pueden describir contexto o resultados observados, pero no demuestran por sí solas implementación municipal ni impacto causal de una política.

**Aclaración:** Los resultados de una encuesta de 2011 no deben presentarse como evidencia actual ni atribuirse a una política implementada posteriormente.

**Aclaración:** Las emergencias coordinadas por el ECU 911 representan eventos de atención operativa y no equivalen automáticamente a delitos denunciados, hechos delictivos confirmados ni resultados de la política municipal.

**Aclaración:** La triangulación de fuentes aumenta la solidez del análisis, pero no corrige automáticamente la ausencia de presupuesto, cobertura, productos, percepción reciente ni evidencia causal.

**Aclaración:** La consistencia interna de la síntesis no sustituye la comprobación humana de las cifras, páginas, definiciones y alcances territoriales en las fuentes originales.

**Aclaración:** La comunicación visual debe simplificar la evidencia sin eliminar sus limitaciones, incertidumbres ni advertencias metodológicas.

**Aclaración:** El enlace del dashboard deberá verificarse nuevamente antes de incorporarlo al informe, al video y al PDF final de entrega.

**Aclaración:** La extensión y reproducción visual de la portada deberán comprobarse en el PDF final antes de la entrega.

**Aclaración:** “El estudiante verificó los enlaces públicos y revisó el PDF definitivo antes de realizar la entrega”.

## Notas finales

### Sobre la revisión documental de F01 (2026-07-21)

El Subagente Verificador de Fuentes completó la extracción y revisión estructural preliminar de la fuente F01 (Plan Metropolitano de Seguridad y Convivencia Ciudadana 2023-2027):

**Resultados de procesamiento:**
- Archivo PDF: 176 páginas totales
- Páginas procesadas con texto extraíble: 163
- Páginas sin contenido de texto: 13 (páginas 2, 3, 6, 9, 16, 18, 19, 56, 128, 154, 160, 175, 176)
- Herramienta utilizada: pypdf (extracción sin OCR)

**Productos generados:**
1. `resultados/plan_metropolitano_texto.txt` - Texto completo extraído con marcadores de página
2. `resultados/plan_metropolitano_metadatos.json` - Metadatos técnicos de la extracción
3. `documentos/indice_verificacion_plan_F01.md` - Índice de verificación con 8 secciones

**Limitaciones documentadas:**
- Extracción automática sin OCR puede omitir gráficos, tablas complejas y contenido visual
- 13 páginas sin contenido de texto requieren revisión directa en PDF original
- Toda cifra, cita o dato debe contrastarse con el PDF original antes de usarse académicamente
- Diferencia crítica: el documento presenta lo **planificado** (2023-2027), no evidencia de lo **ejecutado**

**Aclaración importante:** Esta actividad de revisión estructural **no constituye una verificación completa del contenido ni de las cifras del documento**. Es una identificación preliminar de la estructura documental. La verificación sustantiva de datos, cifras específicas y contenido detallado requiere revisión visual en el PDF original.

### Sobre la validación del Subagente Revisor Crítico (2026-07-21)

La revisión estructural realizada por el Subagente Revisor Crítico sobre los archivos `matriz_fuentes_oficiales.md` e `inventario_fuentes.csv` confirmó:

- Estructura correcta del archivo CSV con exactamente 11 columnas en orden especificado
- Presencia de exactamente 6 registros de fuentes con códigos F01 a F06
- Integridad de campos: todas las filas contienen el número correcto de campos
- Completitud de URLs: ninguna URL fue cortada o modificada
- Identificación clara de F05 como fuente histórica (2011) únicamente para uso como antecedente histórico o metodológico
- Ausencia de marcas falsas de verificación: ninguna fuente está marcada como totalmente verificada
- Consistencia de códigos entre matriz y inventario

**Aclaración importante:** La revisión realizada confirmó la estructura, consistencia de campos, códigos y enlaces registrados, pero no constituye todavía una verificación sustantiva del contenido completo de cada fuente oficial. La verificación de accesibilidad, autenticidad y contenido de fuentes será realizada durante el proceso de recopilación de datos.

### Sobre la auditoría crítica de F01 (2026-07-21)

El Subagente Revisor Crítico completó una auditoría exhaustiva de los hallazgos preliminares contenidos en `indice_verificacion_plan_F01.md`:

**Errores comprobados y corregidos:**

1. **Página inicial de Diagnóstico situacional:** Se corrigió de página 56 a página 57 (página 56 no contiene texto extraíble según metadatos)
2. **Página inicial de Planeación estratégica:** Se corrigió de página 128 a página 129 (página 128 no contiene texto extraíble)
3. **Página inicial de Bibliografía y Glosario:** Se corrigió de página 154 a página 155 (página 154 no contiene texto extraíble)

**Validación de afirmaciones cuantitativas:**

- **4 ejes, 5 objetivos, 8 políticas, 15 programas, 27 proyectos:** Confirmadas parcialmente. Aparecen literalmente en la Presentación del Alcalde (Página 17) pero las tablas de soporte (Tabla 25, Figura 74) no fueron completamente extraídas en formato utilizable para validación numérica completa.

**Riesgos documentados:**

- Las tablas complejas (especialmente Tabla 25) fueron extraídas de forma incompleta/desorganizada
- Las figuras y esquemas (Figura 74, mapas de densidad espacial) no están completamente disponibles en el texto extraído
- **Distinción crítica:** El Plan es documento de PLANIFICACIÓN para 2023-2027, no evidencia de IMPLEMENTACIÓN completada

**Documento de validación:**

Se creó archivo `documentos/validacion_critica_hallazgos_F01.md` con análisis exhaustivo incluyendo tablas de validación, verificación sección por sección, y documentación de riesgos metodológicos.

**Conclusión de auditoría:** La revisión preliminar es ÚTIL COMO GUÍA ESTRUCTURAL pero INSUFICIENTE COMO VALIDACIÓN CUANTITATIVA. Toda cifra específica debe contrastarse directamente con el PDF original antes de incorporarla a análisis académico.

### Sobre la recopilación de datos

Hasta la fecha de este registro (2026-07-21):

- ❌ Los datos estadísticos **no han sido recopilados** de las fuentes oficiales
- ❌ Las fuentes oficiales **no han sido completamente verificadas** en su contenido
- ✅ Las fuentes oficiales **han sido identificadas y documentadas** con sus URLs
- ✅ El marco metodológico **está definido** para guiar la recopilación posterior

### Procedimiento previsto de validación humana

Conforme avance la recopilación de información, toda cifra, interpretación o recomendación generada por los agentes deberá:

1. Contrastarse con la fuente original
2. Ser revisada por el Subagente Verificador de Fuentes
3. Ser examinada por el Subagente Revisor Crítico
4. Ser aceptada, modificada o rechazada por el estudiante
5. Ser registrada en este archivo (registro_agentes.md)

Este documento deberá actualizarse conforme avance el proyecto y se adopten nuevas decisiones. La incorporación de una revisión humana periódica garantiza que el proceso siga siendo riguroso, transparente y adecuado para fines académicos.
