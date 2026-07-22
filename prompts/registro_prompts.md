# Registro de prompts del sistema multiagéntico

## Análisis de la implementación de la política de seguridad ciudadana y recuperación del espacio público en Quito

---

## Tabla resumen de prompts

| Código | Fecha | Agente o rol | Objetivo del prompt | Archivos creados o modificados | Resultado obtenido | Validación realizada | Decisión humana |
|--------|-------|--------------|-------------------|--------------------------------|-------------------|----------------------|-----------------|
| P01 | Anterior a 2026-07-21 | Agente Coordinador | Creación de la estructura inicial del proyecto | Carpetas base, archivos raíz | Estructura del repositorio establecida | Validación de arquitectura | Aceptada |
| P02 | Anterior a 2026-07-21 | Agente Especialista en Políticas Públicas | Documentación de agentes y subagentes | agentes/*.md | Definición de roles de agentes | Revisión de coherencia con objetivos | Aceptada |
| P03 | Anterior a 2026-07-21 | Agente Coordinador | Creación del registro de decisiones | agentes/registro_agentes.md | Estructura de trazabilidad establecida | Validación de formato | Aceptada |
| P04 | Anterior a 2026-07-21 | Agente Programador y Visualización | Creación de main.py | main.py | Punto de entrada funcional | Prueba de ejecución | Aceptada |
| P05 | Anterior a 2026-07-21 | Agente Programador y Visualización | Creación de módulos Python para agentes | agentes/*.py | Módulos multiagénticos operativos | Validación de estructura Python | Aceptada |
| P06 | 2026-07-21 | Agente Coordinador | Creación y corrección de .gitignore | .gitignore | Archivo actualizado para reproducibilidad | Revisión de campos de exclusión | Aceptada |
| P07 | 2026-07-21 | Agente Especialista en Políticas Públicas | Creación de README en carpetas vacías | datos/README.md, documentos/README.md, dashboard/README.md, prompts/README.md, resultados/README.md, src/README.md | Documentación de propósito y contenido esperado | Revisión de completitud y claridad | Aceptada |
| P08 | 2026-07-21 | Agente Especialista en Políticas Públicas | Actualización del README principal | README.md | Documentación académica profesional del proyecto | Revisión de secciones y alineación con diseño | Aceptada |
| P09 | 2026-07-21 | Agente de Datos y Metodología | Creación del diseño metodológico detallado | documentos/diseno_metodologico.md | Matriz metodológica y criterios de interpretación definidos | Revisión crítica de dimensiones y limitaciones | Aceptada |
| P10 | 2026-07-21 | Agente de Datos y Metodología | Creación de matriz e inventario de fuentes | documentos/matriz_fuentes_oficiales.md, datos/inventario_fuentes.csv | Seis fuentes oficiales registradas y documentadas | Validación estructural de campos y URLs | Aceptada |
| P11 | 2026-07-21 | Subagente Revisor Crítico | Validación estructural de archivos de fuentes | Revisión de matriz_fuentes_oficiales.md e inventario_fuentes.csv | Confirmación de consistencia, integridad y advertencias | Verificación de 7 criterios de calidad | Aceptada |

---

## P01: Creación de la estructura inicial del proyecto

**Agente responsable:** Agente Coordinador

**Tarea solicitada:** Crear la estructura base del repositorio con carpetas y archivos raíz necesarios para el proyecto académico multiagéntico.

**Prompt principal:**

```
Quiero crear un proyecto académico en Python sobre análisis de implementación de una política pública.

El proyecto tratará sobre la implementación de la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito.

Necesito que generes una estructura profesional del proyecto con carpetas para:
- datos
- documentos
- dashboard
- agentes
- prompts
- resultados
- src

Además crea un archivo README.md explicando el proyecto y un archivo requirements.txt con las dependencias iniciales.
```

**Resultado:**

Repositorio estructurado con arquitectura profesional y escalable, incluyendo carpetas temáticas para diferentes tipos de contenido y funcionalidades.

**Archivos afectados:**

- main.py
- requirements.txt
- README.md (versión inicial)
- .gitkeep en carpetas vacías
- Estructura de directorios base

**Revisión aplicada:**

Validación de coherencia arquitectónica con los objetivos del análisis académico.

**Decisión humana:**

Aceptada

---

## P02: Documentación de agentes y subagentes

**Agente responsable:** Agente Especialista en Políticas Públicas

**Tarea solicitada:** Crear documentación en Markdown de cada agente y subagente, describiendo sus funciones, responsabilidades y metodología.

**Prompt principal:**

```
Quiero desarrollar un proyecto académico sobre el análisis de implementación de una política pública.

Necesito crear una arquitectura multiagéntica profesional.

Crea la estructura completa de agentes y subagentes en la carpeta "agentes".

Los agentes serán:

1. Agente Coordinador
Responsabilidad:
- Planificar el proyecto.
- Asignar tareas.
- Coordinar el trabajo de todos los agentes.
- Registrar decisiones.

2. Agente Especialista en Políticas Públicas
Responsabilidad:
- Analizar el problema público.
- Analizar instituciones.
- Analizar actores.
- Analizar el ciclo de la política pública.
- Revisar normativa.

3. Agente de Datos y Metodología
Responsabilidad:
- Organizar bases de datos.
- Analizar indicadores.
- Definir metodología.
- Elaborar tablas.

4. Agente Programador y Visualización
Responsabilidad:
- Construir el dashboard.
- Programar el proyecto.
- Generar gráficos.

Subagente 1
Verificador de fuentes y normativa.
Debe revisar que todas las cifras, leyes, documentos y referencias sean oficiales.

Subagente 2
Revisor crítico.
Debe detectar errores metodológicos, conceptuales y técnicos antes de aceptar cualquier resultado.

Genera un archivo independiente para cada agente utilizando Markdown (.md).

Cada archivo debe incluir:

- Objetivo
- Responsabilidades
- Entradas
- Salidas
- Prompt principal
- Ejemplos de uso
- Flujo de trabajo
```

**Resultado:**

Documentación clara de roles y responsabilidades de cada componente del sistema multiagéntico.

**Archivos afectados:**

- agentes/agente-coordinador.md
- agentes/agente-politicas-publicas.md
- agentes/agente-datos-metodologia.md
- agentes/agente-programador-visualizacion.md
- agentes/subagente-verificador-fuentes.md
- agentes/subagente-revisor-critico.md

**Revisión aplicada:**

Coherencia con los objetivos del proyecto y claridad de funciones dentro de la arquitectura.

**Decisión humana:**

Aceptada

---

## P03: Creación del registro de decisiones

**Agente responsable:** Agente Coordinador

**Tarea solicitada:** Crear archivo de registro formal de decisiones adoptadas durante el desarrollo del proyecto.

**Prompt principal:**

```
Crea un archivo llamado registro_agentes.md dentro de la carpeta agentes.

Este archivo debe documentar todas las decisiones tomadas durante el proyecto.

Incluye una tabla con las siguientes columnas:

- Fecha
- Agente responsable
- Tarea realizada
- Resultado obtenido
- Observaciones
- Decisión (Aceptada o Rechazada)
- Validación humana

Agrega además una breve explicación sobre la importancia de registrar las decisiones en un sistema multiagéntico aplicado al análisis de políticas públicas.

El formato debe ser profesional y listo para incluirse como evidencia en el informe académico.
```

**Resultado:**

Archivo de registro operativo que permite documentar y auditar todas las decisiones del sistema multiagéntico.

**Archivos afectados:**

- agentes/registro_agentes.md

**Revisión aplicada:**

Validación de estructura y utilidad para trazabilidad académica.

**Decisión humana:**

Aceptada

---

## P04: Creación de main.py

**Agente responsable:** Agente Programador y Visualización

**Tarea solicitada:** Crear archivo principal del proyecto que sirva como punto de entrada y ejecute el Agente Coordinador.

**Prompt principal:**

```
Quiero comenzar el desarrollo del proyecto.

Crea el archivo main.py en la raíz del proyecto.

El archivo debe:

- Ser el punto de entrada del proyecto.
- Mostrar un menú principal en consola.
- Mostrar el título:
  "Sistema Multiagéntico para el Análisis de Implementación de la Política de Seguridad Ciudadana y Recuperación del Espacio Público del Distrito Metropolitano de Quito".

El menú debe tener las siguientes opciones:

1. Ejecutar Agente Coordinador.
2. Ejecutar Agente de Políticas Públicas.
3. Ejecutar Agente de Datos y Metodología.
4. Ejecutar Agente de Programación y Visualización.
5. Ejecutar Subagente Verificador.
6. Ejecutar Subagente Revisor Crítico.
7. Salir.

Cada opción debe mostrar temporalmente un mensaje indicando qué agente fue seleccionado.

El código debe estar organizado y comentado, listo para futuras ampliaciones.
```

**Resultado:**

Punto de entrada funcional del proyecto mediante `python main.py` o `py main.py`.

**Archivos afectados:**

- main.py

**Revisión aplicada:**

Prueba local de ejecución correcta del Agente Coordinador.

**Decisión humana:**

Aceptada

---

## P05: Creación de módulos Python para agentes

**Agente responsable:** Agente Programador y Visualización

**Tarea solicitada:** Convertir documentación de agentes en módulos Python ejecutables.

**Prompt principal:**

```
Ahora quiero convertir el proyecto en un sistema funcional.

Realiza las siguientes tareas:

1. Crea un archivo __init__.py dentro de la carpeta agentes.

2. Convierte cada archivo de agente en un módulo de Python (.py) conservando también la documentación en Markdown.

Crea los siguientes archivos:

- agente_coordinador.py
- agente_politicas_publicas.py
- agente_datos_metodologia.py
- agente_programador_visualizacion.py
- subagente_verificador_fuentes.py
- subagente_revisor_critico.py

Cada archivo debe contener una función llamada ejecutar().

Cuando se ejecute debe imprimir en consola:

- Nombre del agente.
- Objetivo.
- Responsabilidades principales.
- Estado: "Agente ejecutado correctamente."

No elimines los archivos .md existentes.

Organiza el código siguiendo buenas prácticas para que posteriormente pueda ser importado desde main.py.
```

**Resultado:**

Arquitectura multiagéntica operativa implementada en Python con módulos especializados.

**Archivos afectados:**

- agentes/agente_coordinador.py
- agentes/agente_politicas_publicas.py
- agentes/agente_datos_metodologia.py
- agentes/agente_programador_visualizacion.py
- agentes/subagente_verificador_fuentes.py
- agentes/subagente_revisor_critico.py
- agentes/__init__.py

**Revisión aplicada:**

Validación de estructura Python y consistencia con documentación.

**Decisión humana:**

Aceptada

---

## P06: Creación y corrección de .gitignore

**Agente responsable:** Agente Coordinador

**Tarea solicitada:** Crear archivo .gitignore con reglas de exclusión apropiadas para el proyecto, y luego corregirlo para mejorar reproducibilidad.

**Prompt principal:**

```
Prepara el proyecto para publicarlo de forma segura en GitHub.

Crea un archivo .gitignore en la raíz del proyecto.

Debe excluir:

- __pycache__/
- *.pyc
- .venv/
- venv/
- .env
- .env.*
- .vscode/
- node_modules/
- .next/
- dist/
- build/
- archivos temporales del sistema operativo

No debe excluir:

- los archivos Python del proyecto;
- los documentos Markdown;
- las carpetas agentes, datos, documentos, dashboard, prompts, resultados y src;
- los archivos CSV o JSON públicos que posteriormente utilizaremos.

Agrega comentarios dentro del archivo .gitignore para identificar cada grupo de exclusiones.

No elimines ni modifiques los demás archivos.
```

**Resultado:**

Archivo .gitignore creado con 11 grupos de exclusiones comentados. Posteriormente se corrigió eliminando package-lock.json y yarn.lock para asegurar reproducibilidad del dashboard.

**Archivos afectados:**

- .gitignore (creado y modificado)

**Revisión aplicada:**

Verificación de coherencia de reglas de exclusión con objetivos de seguridad y reproducibilidad del proyecto.

**Decisión humana:**

Aceptada

---

## P07: Creación de README en carpetas vacías

**Agente responsable:** Agente Especialista en Políticas Públicas

**Tarea solicitada:** Crear archivo README.md en cada carpeta del proyecto para documentar su propósito, tipos de archivos esperados y requisitos de documentación.

**Prompt principal:**

```
Prepara las carpetas del proyecto para que puedan conservarse y documentarse correctamente en GitHub.

Revisa estas carpetas:

- datos
- documentos
- dashboard
- prompts
- resultados
- src

Si alguna no contiene archivos, crea dentro de ella un archivo README.md.

Cada README.md debe explicar brevemente:

- el propósito de la carpeta;
- qué tipos de archivos se almacenarán;
- que los datos, documentos o resultados incorporados deberán estar correctamente documentados.

No elimines ni reemplaces archivos existentes.
No modifiques el README.md principal.
No modifiques ningún archivo fuera de estas carpetas.
```

**Resultado:**

Seis archivos README.md creados, uno por carpeta, con descripción de propósito, tipos de contenido y requisitos de documentación.

**Archivos afectados:**

- datos/README.md
- documentos/README.md
- dashboard/README.md
- prompts/README.md
- resultados/README.md
- src/README.md

**Revisión aplicada:**

Validación de claridad y completitud de instrucciones de documentación para futuros contenidos.

**Decisión humana:**

Aceptada

---

## P08: Actualización del README principal

**Agente responsable:** Agente Especialista en Políticas Públicas

**Tarea solicitada:** Reemplazar el README.md inicial con documentación académica profesional que incluya 16 secciones especificadas sobre el proyecto.

**Prompt principal:**

```
Actualiza únicamente el archivo README.md principal de la raíz del proyecto.

Redáctalo en español, con estilo académico, profesional y claro.

El README debe incluir las siguientes secciones:

1. Título del proyecto
"Análisis de la implementación de la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito".

2. Descripción general
Explica que es un proyecto académico individual desarrollado mediante una arquitectura multiagéntica de inteligencia artificial.

3. Modalidad
Análisis de implementación de una política pública.

4. Problema público
El aumento de la percepción de inseguridad y de los delitos de oportunidad en zonas comerciales, parques y paradas de transporte público del Distrito Metropolitano de Quito.

5. Pregunta central
¿Cómo se ha implementado la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito, y cuáles han sido sus principales resultados y desafíos?

6. Objetivo general
Analizar la implementación de la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito, mediante la revisión de información oficial y documentos institucionales, para identificar fortalezas, limitaciones y oportunidades de mejora.

7. Instituciones y actores
- Municipio del Distrito Metropolitano de Quito.
- Policía Nacional del Ecuador.
- ECU 911.
- Ciudadanía y comerciantes.

8. Fuentes previstas
- Municipio de Quito.
- Policía Nacional.
- INEC.
- ECU 911.
- Plan Metropolitano de Seguridad Ciudadana.

Aclara que las fuentes y bases de datos todavía se encuentran en proceso de recopilación y verificación.

9. Indicadores previstos
- Insumo: presupuesto destinado a seguridad ciudadana.
- Producto: cámaras, luminarias y alarmas comunitarias instaladas.
- Resultado: variación de delitos registrados y percepción de seguridad.

10. Metodología
Explica que se aplicará análisis de implementación mediante revisión documental, análisis de ejecución, cobertura, recursos, coordinación institucional y resultados.

Aclara que el proyecto no realizará una evaluación causal de impacto.

11. Arquitectura multiagéntica
Describe brevemente:
- Agente coordinador.
- Agente especialista en políticas públicas.
- Agente de datos y metodología.
- Agente de programación y visualización.
- Subagente verificador de fuentes.
- Subagente revisor crítico.

12. Estructura del repositorio
Explica brevemente para qué sirve cada carpeta principal.

13. Ejecución local
Incluye las instrucciones:

python main.py

Y como alternativa para Windows:

py main.py

14. Estado actual
Indica que la estructura inicial y los módulos de agentes están implementados, pero que la recopilación de datos, el análisis y el dashboard están en desarrollo.

15. Enlaces del proyecto
Crea espacios pendientes para:
- Dashboard en Vercel.
- Informe académico.
- Video de demostración.

16. Autoría y responsabilidad
Explica que el estudiante es responsable de verificar los datos, revisar los resultados generados por IA y justificar las decisiones metodológicas.

No inventes estadísticas, resultados, enlaces, fechas, presupuestos ni cifras.
No modifiques ningún otro archivo.
```

**Resultado:**

README.md reescrito como documento académico de 16 secciones con descripción clara del proyecto, metodología, arquitectura multiagéntica y estado actual.

**Archivos afectados:**

- README.md

**Revisión aplicada:**

Validación de alineación con objetivos académicos, claridad de secciones y ausencia de información inventada.

**Decisión humana:**

Aceptada

---

## P09: Creación del diseño metodológico detallado

**Agente responsable:** Agente de Datos y Metodología

**Tarea solicitada:** Crear documento exhaustivo de diseño metodológico incluyendo modalidad, unidad de análisis, delimitaciones, objetivos, dimensiones de análisis, matriz metodológica, limitaciones y procedimientos de validación.

**Prompt principal:**

```
Crea un archivo llamado diseno_metodologico.md dentro de la carpeta documentos.

El documento debe desarrollar el diseño metodológico del proyecto:

"Análisis de la implementación de la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito".

Debe redactarse en español, con estilo académico y profesional.

Incluye las siguientes secciones:

1. Modalidad del proyecto
Indica que corresponde a un análisis de implementación y no a una evaluación causal de impacto.

2. Unidad de análisis
Define como unidad de análisis la implementación del Plan Metropolitano de Seguridad y Convivencia Ciudadana 2023-2027 y las estrategias municipales relacionadas con seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito.

3. Delimitación temporal
Establece como periodo principal de análisis 2023-2025, debido a que permite trabajar con años completos de implementación.
Aclara que la información de 2026 podrá utilizarse únicamente si se encuentra completa y oficialmente publicada.

4. Delimitación territorial
Distrito Metropolitano de Quito, con atención especial a:
- zonas comerciales;
- parques;
- paradas de transporte público;
- sectores en los que existan intervenciones documentadas.

5. Pregunta central
¿Cómo se ha implementado la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito, y cuáles han sido sus principales resultados y desafíos?

6. Objetivo general
Analizar la implementación de la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito, mediante la revisión de información oficial y documentos institucionales, para identificar fortalezas, limitaciones y oportunidades de mejora.

7. Objetivos específicos
Formula cuatro objetivos específicos relacionados con:
- marco institucional y normativo;
- recursos y acciones ejecutadas;
- coordinación, cobertura y productos;
- fortalezas, limitaciones y recomendaciones.

8. Enfoque metodológico
Explica que se utilizará:
- revisión documental;
- análisis descriptivo de indicadores;
- comparación temporal cuando existan datos comparables;
- triangulación de fuentes institucionales;
- análisis cualitativo de coordinación, gestión y dificultades.

9. Dimensiones del análisis de implementación
Desarrolla las siguientes dimensiones:
- diseño y planificación;
- instituciones y competencias;
- recursos y presupuesto;
- actividades ejecutadas;
- coordinación interinstitucional;
- cobertura territorial y poblacional;
- productos entregados;
- resultados inmediatos;
- participación ciudadana;
- equidad territorial;
- transparencia y rendición de cuentas.

10. Matriz metodológica
Incluye una tabla con estas columnas:
- Dimensión.
- Pregunta de análisis.
- Indicador previsto.
- Evidencia necesaria.
- Fuente institucional prevista.
- Método de análisis.
- Limitación posible.
- Estado de verificación.

Las fuentes institucionales previstas deben incluir:
- Municipio del Distrito Metropolitano de Quito;
- Secretaría responsable de seguridad;
- Policía Nacional del Ecuador;
- ECU 911;
- INEC;
- Observatorio Metropolitano de Seguridad Ciudadana;
- documentos normativos oficiales.

11. Criterios de interpretación
Diferencia claramente:
- insumos;
- actividades;
- productos;
- resultados;
- impacto causal.

Aclara que una variación de delitos o percepción no demuestra por sí sola que la política haya causado ese cambio.

12. Limitaciones metodológicas previstas
Incluye:
- ausencia de datos desagregados;
- diferencias entre periodos y fuentes;
- subregistro de delitos;
- datos de percepción posiblemente desactualizados;
- dificultad para atribuir resultados a una sola institución;
- información presupuestaria incompleta;
- diferencias entre emergencias reportadas y delitos denunciados.

13. Procedimiento de validación humana
Explica que toda cifra, interpretación o recomendación generada por los agentes deberá:
- contrastarse con la fuente original;
- ser revisada por el subagente verificador;
- ser examinada por el subagente crítico;
- ser aceptada o rechazada por el estudiante;
- registrarse en el archivo registro_agentes.md.

14. Estado del documento
Aclara que el diseño metodológico está definido, pero que los indicadores y resultados serán completados después de recopilar y verificar las fuentes oficiales.

No inventes estadísticas, presupuestos, resultados, nombres de programas específicos ni cifras.
No agregues referencias bibliográficas inexistentes.
No modifiques ningún otro archivo.
```

**Resultado:**

Documento exhaustivo de 14 secciones incluyendo matriz metodológica de 11 dimensiones, criterios de interpretación, limitaciones previstas y procedimiento de validación humana.

**Archivos afectados:**

- documentos/diseno_metodologico.md

**Revisión aplicada:**

Verificación de rigor metodológico, claridad de definiciones y coherencia entre dimensiones e indicadores.

**Decisión humana:**

Aceptada

---

## P10: Creación de matriz e inventario de fuentes

**Agente responsable:** Agente de Datos y Metodología

**Tarea solicitada:** Crear matriz de fuentes oficiales y archivo CSV de inventario documentando 6 fuentes institucionales con URLs, tipos, periodos y limitaciones.

**Prompt principal:**

```
Crea dos archivos para documentar las fuentes oficiales del proyecto:

1. documentos/matriz_fuentes_oficiales.md
2. datos/inventario_fuentes.csv

No modifiques ningún otro archivo.

TÍTULO:
Matriz de fuentes oficiales para el análisis de implementación de la política de seguridad ciudadana y recuperación del espacio público en Quito.

FUENTES QUE DEBEN REGISTRARSE:

1. Plan Metropolitano de Seguridad y Convivencia Ciudadana 2023-2027
Institución: Municipio del Distrito Metropolitano de Quito
Tipo: Plan de política pública
URL:
https://seguridad.quito.gob.ec/wp-content/uploads/2024/12/Plan-Metropolitano-de-Seguridad-Ciudadana-Version-Web.pdf

2. Seguimiento al Plan Metropolitano de Seguridad y Convivencia Ciudadana 2023-2027
Institución: Observatorio Metropolitano de Seguridad Ciudadana
Tipo: Portal de seguimiento
URL:
https://observatorioseguridad.quito.gob.ec/seguimiento-al-plan-metropolitano-de-seguridad-y-convivencia-ciudadana-2023-2027/

3. Resolución ADMQ 008-2024
Institución: Municipio del Distrito Metropolitano de Quito
Tipo: Norma y resolución de implementación
URL:
https://www7.quito.gob.ec/mdmq_ordenanzas/Administraci%C3%B3n%202023-2027/Resoluciones%20de%20Alcald%C3%ADa/2024/RADMQ-008-2024%20-%20Implementaci%C3%B3n%20del%20Plan%20Metropolitano%20de%20Seguridad%20y%20Convivencia%20Ciudadana%202023-2027.pdf

4. Justicia y crimen
Institución: Instituto Nacional de Estadística y Censos
Tipo: Portal estadístico
URL:
https://www.ecuadorencifras.gob.ec/justicia-y-crimen/

5. Encuesta de Victimización y Percepción de Inseguridad 2011
Institución: Instituto Nacional de Estadística y Censos
Tipo: Encuesta y base estadística
URL:
https://anda.inec.gob.ec/anda5/index.php/catalog/673

Aclara que esta encuesta corresponde al año 2011 y solamente podrá utilizarse como antecedente histórico o metodológico, no como evidencia actual de percepción de inseguridad.

6. Estadísticas de emergencias coordinadas en 2024
Institución: Servicio Integrado de Seguridad ECU 911
Tipo: Informe y estadística institucional
URL:
https://www.ecu911.gob.ec/el-ecu-911-coordino-la-atencion-de-mas-de-3-millones-de-emergencias-en-2024/

ESTRUCTURA DE matriz_fuentes_oficiales.md:

Incluye una tabla con las columnas:

- Código de fuente
- Nombre del documento o portal
- Institución responsable
- Tipo de fuente
- Periodo disponible
- Variables o información esperada
- Utilidad para el proyecto
- Limitaciones
- Nivel territorial
- Enlace oficial
- Estado de revisión
- Fecha de consulta
- Decisión del estudiante

Utiliza los códigos:

- F01
- F02
- F03
- F04
- F05
- F06

En "Estado de revisión" coloca:
"Fuente identificada; contenido pendiente de extracción y verificación".

En "Fecha de consulta" coloca:
"Pendiente de registro por el estudiante".

En "Decisión del estudiante" coloca:
"Pendiente".

Agrega después de la tabla:

1. Criterios de selección de fuentes.
2. Procedimiento para verificar autenticidad.
3. Diferencias entre:
   - delitos denunciados;
   - emergencias atendidas;
   - percepción de inseguridad;
   - actividades municipales;
   - productos de la política.
4. Advertencia metodológica indicando que estos conceptos no deben sumarse ni compararse directamente sin revisar su definición y periodo.
5. Procedimiento de actualización de la matriz.

ESTRUCTURA DE inventario_fuentes.csv:

Debe utilizar estas columnas:

codigo_fuente,nombre_fuente,institucion,tipo_fuente,periodo,nivel_territorial,url,estado_revision,fecha_consulta,decision_estudiante,observaciones

Registra las seis fuentes indicadas.

REQUISITOS:

- No inventes cifras.
- No inventes fechas de consulta.
- No afirmes que los datos ya fueron descargados.
- No marques ninguna fuente como completamente verificada.
- No extraigas todavía información estadística.
- Mantén los enlaces exactamente como fueron proporcionados.
- Utiliza codificación UTF-8.
```

**Resultado:**

Dos archivos creados: matriz de fuentes en Markdown con tabla de 6 fuentes y 5 secciones de criterios y procedimientos; inventario en CSV con 11 columnas y 6 registros de fuentes oficiales.

**Archivos afectados:**

- documentos/matriz_fuentes_oficiales.md
- datos/inventario_fuentes.csv

**Revisión aplicada:**

Validación de completitud de URLs, códigos consistentes F01-F06, advertencias sobre diferencias conceptuales y ausencia de marcas falsas de verificación.

**Decisión humana:**

Aceptada

---

## P11: Validación estructural del Subagente Revisor Crítico

**Agente responsable:** Subagente Revisor Crítico

**Tarea solicitada:** Realizar verificaciones de calidad sobre los archivos de matriz de fuentes y inventario, confirmando estructura, integridad de campos, URLs completas y advertencias metodológicas.

**Prompt principal:**

```
Actúa como Subagente Revisor Crítico y verifica únicamente estos archivos:

- documentos/matriz_fuentes_oficiales.md
- datos/inventario_fuentes.csv

Realiza las siguientes comprobaciones:

1. Confirma que inventario_fuentes.csv tenga exactamente estas 11 columnas y en este orden:

codigo_fuente,nombre_fuente,institucion,tipo_fuente,periodo,nivel_territorial,url,estado_revision,fecha_consulta,decision_estudiante,observaciones

2. Confirma que existan exactamente seis registros de fuentes, con los códigos:
F01, F02, F03, F04, F05 y F06.

3. Confirma que todas las filas tengan el mismo número de campos que el encabezado.

4. Confirma que las URLs estén completas y no hayan sido cortadas o modificadas.

5. Confirma que la fuente F05 indique expresamente que corresponde a 2011 y que únicamente puede utilizarse como antecedente histórico o metodológico.

6. Confirma que ninguna fuente esté marcada como totalmente verificada.

7. Verifica que matriz_fuentes_oficiales.md contenga las seis fuentes y que sus códigos coincidan con el archivo CSV.

8. Corrige únicamente los errores que realmente encuentres.

9. No inventes información, fechas, cifras ni estados de verificación.

10. No modifiques ningún otro archivo.

Al finalizar, presenta un informe breve indicando:
- comprobaciones realizadas;
- errores encontrados;
- correcciones aplicadas;
- resultado final de la validación.
```

**Resultado:**

Validación exitosa de ambos archivos sin errores encontrados. Confirmadas: 11 columnas en orden correcto, 6 registros con códigos F01-F06, integridad de campos por fila, URLs completas, advertencia clara de F05 como antecedente histórico 2011, ninguna fuente marcada como verificada, códigos coincidentes entre archivos.

**Archivos afectados:**

- documentos/matriz_fuentes_oficiales.md (revisado)
- datos/inventario_fuentes.csv (revisado)

**Revisión aplicada:**

La revisión realizada confirmó la estructura, consistencia de campos, códigos y enlaces registrados, pero no constituye todavía una verificación sustantiva del contenido completo de cada fuente oficial.

**Decisión humana:**

Aceptada

---

**Documento compilado:** 2026-07-21  
**Total de prompts registrados:** 11 (P01-P11)  
**Prompts de sesión actual:** 6 (P06-P11)  
**Estado:** Completo
