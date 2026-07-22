# Análisis de la implementación de la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito

## Descripción general

Este es un proyecto académico individual desarrollado mediante una arquitectura multiagéntica de inteligencia artificial. El proyecto aplica un enfoque innovador que combina análisis de implementación de políticas públicas con sistemas autónomos inteligentes para sistematizar, procesar y sintetizar información institucional.

## Modalidad

Análisis de implementación de una política pública.

## Problema público

El aumento de la percepción de inseguridad y de los delitos de oportunidad en zonas comerciales, parques y paradas de transporte público del Distrito Metropolitano de Quito constituye una problemática que ha requerido respuestas institucionales articuladas. La falta de análisis sistemático sobre la implementación de políticas de seguridad ciudadana dificulta la identificación de fortalezas, limitaciones y oportunidades de mejora en las acciones desplegadas.

## Pregunta central

¿Cómo se ha implementado la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito, y cuáles han sido sus principales resultados y desafíos?

## Objetivo general

Analizar la implementación de la política de seguridad ciudadana y recuperación del espacio público en el Distrito Metropolitano de Quito, mediante la revisión de información oficial y documentos institucionales, para identificar fortalezas, limitaciones y oportunidades de mejora.

## Instituciones y actores

- Municipio del Distrito Metropolitano de Quito
- Policía Nacional del Ecuador
- ECU 911
- Ciudadanía y comerciantes

## Fuentes previstas

- Municipio de Quito
- Policía Nacional
- INEC (Instituto Nacional de Estadística y Censos)
- ECU 911
- Plan Metropolitano de Seguridad Ciudadana

**Nota importante:** Las fuentes y bases de datos se encuentran actualmente en proceso de recopilación y verificación. La disponibilidad y accesibilidad de la información oficial podrá condicionar el alcance del análisis.

## Indicadores previstos

- **Insumo:** Presupuesto destinado a seguridad ciudadana
- **Producto:** Cámaras, luminarias y alarmas comunitarias instaladas
- **Resultado:** Variación de delitos registrados y percepción de seguridad

## Metodología

Se aplicará un **análisis de implementación** mediante revisión documental y análisis de:

- **Ejecución:** Actividades y acciones realizadas en comparación con lo planeado
- **Cobertura:** Alcance geográfico y poblacional de las intervenciones
- **Recursos:** Asignación y utilización de recursos presupuestarios y materiales
- **Coordinación institucional:** Articulación entre actores y niveles de gobierno
- **Resultados:** Cambios observados en indicadores de seguridad y espacio público

**Aclaración metodológica:** Este proyecto **no realizará una evaluación causal de impacto**. El análisis se enfoca en caracterizar la implementación y sus resultados, no en atribuir causalidad directa entre intervenciones y cambios en indicadores de seguridad.

## Arquitectura multiagéntica

El proyecto utiliza una arquitectura de inteligencia artificial multiagéntica compuesta por:

- **Agente coordinador:** Orquesta el flujo de trabajo, distribuye tareas y coordina la comunicación entre agentes especializados
- **Agente especialista en políticas públicas:** Analiza documentos de política, identifica lineamientos, objetivos y diseño de intervenciones
- **Agente de datos y metodología:** Procesa información cuantitativa, valida datos y aplica análisis metodológicos
- **Agente de programación y visualización:** Genera visualizaciones, dashboards interactivos y reportes técnicos
- **Subagente verificador de fuentes:** Valida la calidad, procedencia y confiabilidad de las fuentes de información utilizadas
- **Subagente revisor crítico:** Examina críticamente los análisis, identifica supuestos, limitaciones y posibles sesgos

## Estructura del repositorio

```
├── main.py                          # Punto de entrada del proyecto
├── requirements.txt                 # Dependencias de Python
├── README.md                        # Este archivo
├── agentes/                         # Módulos de agentes inteligentes
│   ├── agente_coordinador.py
│   ├── agente_politicas_publicas.py
│   ├── agente_datos_metodologia.py
│   ├── agente_programador_visualizacion.py
│   ├── subagente_verificador_fuentes.py
│   └── subagente_revisor_critico.py
├── datos/                           # Datasets, archivos de entrada y bases de datos
├── documentos/                      # Informes, referencias y documentación
├── dashboard/                       # Componentes y recursos de visualización
├── prompts/                         # Instrucciones y plantillas para agentes
├── resultados/                      # Salidas, reportes y análisis generados
└── src/                             # Código fuente y módulos auxiliares
```

**Descripción de carpetas:**

- **agentes/:** Implementación de la arquitectura multiagéntica con módulos especializados
- **datos/:** Almacenamiento de datasets, archivos CSV, JSON y bases de datos utilizadas en el análisis
- **documentos/:** Documentación de referencia, políticas públicas, artículos académicos e informes institucionales
- **dashboard/:** Código frontend, componentes de visualización e interfaces interactivas
- **prompts/:** Instrucciones, plantillas y directrices para la operación de agentes inteligentes
- **resultados/:** Reportes finales, tablas de síntesis, gráficos y análisis generados por los agentes
- **src/:** Funciones auxiliares, módulos reutilizables y utilidades de programación

## Ejecución local

Para ejecutar el proyecto, utiliza:

```bash
python main.py
```

En sistemas Windows, también puedes usar:

```bash
py main.py
```

Asegúrate de haber instalado las dependencias del proyecto antes de ejecutarlo. Consulta `requirements.txt` para más detalles.

## Estado actual

- ✅ **Completado:** Estructura inicial del proyecto y módulos de agentes
- 🔄 **En desarrollo:** Recopilación de datos y análisis integrado
- ✅ **Dashboard:** Dashboard funcional, probado localmente y desplegado en Vercel

La arquitectura multiagéntica está implementada y operativa. Se encuentra en fase de integración de fuentes de información y generación de análisis preliminares.

## Enlaces del proyecto

- **Repositorio:** [https://github.com/danny19052005/ProyectoFinal_PoliticasPublicas](https://github.com/danny19052005/ProyectoFinal_PoliticasPublicas)
- **Dashboard:** [https://proyecto-final-politicas-publicas-gh42niquf.vercel.app/](https://proyecto-final-politicas-publicas-gh42niquf.vercel.app/)
- **Informe académico completo:** pendiente
- **Video de demostración:** pendiente
- **PDF final de entrega:** pendiente

## Autoría y responsabilidad

El estudiante es **responsable de:**

- Verificar la confiabilidad e integridad de los datos utilizados en el análisis
- Revisar críticamente los resultados generados por los agentes de inteligencia artificial
- Justificar las decisiones metodológicas adoptadas en el análisis
- Documentar limitaciones, supuestos y posibles sesgos en los hallazgos
- Asegurar el cumplimiento de estándares académicos y éticos

Los agentes inteligentes operan como herramientas de apoyo y sistematización. La responsabilidad intelectual y académica del análisis recae en el estudiante.
