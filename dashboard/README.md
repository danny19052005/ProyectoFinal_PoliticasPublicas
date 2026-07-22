# Dashboard académico de implementación (F01-F06)

## Propósito

Este dashboard presenta de forma visual, académica y prudente la síntesis integrada y auditada del análisis de implementación de la política de seguridad ciudadana y recuperación del espacio público en Quito. Su objetivo es comunicar evidencia documental, estados cualitativos, hallazgos, limitaciones y advertencias metodológicas sin sobreinterpretar resultados.

## Datos utilizados

Fuente principal de datos del dashboard:

- `dashboard/data/resumen_dashboard_F01_F06.json`

Este archivo es una copia controlada del resumen auditado en:

- `resultados/resumen_dashboard_F01_F06.json`

Respaldo documental:

- `documentos/sintesis_integrada_implementacion_F01_F06.md`
- `documentos/validacion_critica_sintesis_integrada_F01_F06.md`
- `datos/matriz_integrada_implementacion_F01_F06.csv`

## Archivos del dashboard

- `dashboard/index.html`: estructura semántica y secciones del dashboard.
- `dashboard/styles.css`: diseño visual responsive, etiquetas de estado, filtros y estilos de impresión.
- `dashboard/script.js`: carga local del JSON, render dinámico y filtros.
- `dashboard/vercel.json`: configuración estática para despliegue del subdirectorio dashboard.
- `dashboard/data/resumen_dashboard_F01_F06.json`: dataset local auditado para visualización.

## Ejecución local

Comando:

```powershell
py -m http.server 8000 --directory dashboard
```

Abrir en navegador:

```text
http://localhost:8000
```

## Despliegue en Vercel

Este repositorio incluye un archivo `vercel.json` en la raíz con `outputDirectory: "dashboard"` para publicar el sitio estático desde la raíz sin detectar `main.py` como aplicación Python.

Alternativamente, también puede seleccionarse `dashboard` como Root Directory en Vercel. En ambos casos:

- no se requiere instalación;
- no se requiere build;
- no se requieren funciones;
- no se usa Node, npm ni Python para el despliegue del frontend.

## Despliegue público

- Estado: desplegado correctamente.
- Plataforma: Vercel.
- Enlace público activo: https://proyecto-final-politicas-publicas-gh42niquf.vercel.app/
- Repositorio conectado: https://github.com/danny19052005/ProyectoFinal_PoliticasPublicas
- Fecha de registro: 2026-07-22.

Los nuevos commits en la rama main pueden generar actualizaciones automáticas del despliegue.

## Sincronización del JSON

Cuando cambie `resultados/resumen_dashboard_F01_F06.json`, debe sincronizarse la copia de `dashboard/data/resumen_dashboard_F01_F06.json` para mantener coherencia visual con la versión auditada.

## Limitaciones metodológicas

El dashboard refleja un análisis de implementación, no una evaluación causal de impacto. Se mantienen explícitas las advertencias sobre:

- diferencias de definición y periodo;
- cobertura territorial incompleta;
- evidencia presupuestaria parcial o limitada;
- F04 sin cifras específicas verificadas de Quito en el texto analizado;
- F05 como antecedente histórico de 2011;
- F06 como registro operativo de emergencias y no de delitos;
- imposibilidad de atribuir cambios a una sola institución sin diseño causal.

## Advertencia de uso

No deben presentarse datos pendientes o parciales como resultados confirmados de efectividad, cumplimiento total, éxito o fracaso general de la política.
