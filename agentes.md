# Agentes del proyecto

Este proyecto es un trabajo de titulación enfocado en aplicar modelos de transformers a datos tabulares y comparar su desempeño con un baseline de Random Forest.

## Contexto del problema

- Dataset: eventos sísmicos del volcán Cotopaxi.
- Objetivo: clasificar el tipo de evento sísmico.
- Variable objetivo: `type`, que representa el tipo de evento.
  - Ejemplos: `VT` (Volcano-Tectonic), `LP` (Long-Period), entre otros.

## Características del dataset

- Variables categóricas:
  - `type` (tipo de evento sísmico)
- Variables temporales:
  - Prefijo `t_`
- Variables frecuenciales:
  - Prefijo `f_`
- Variables de wavelet:
  - Prefijo `w_`

## Enfoque técnico

- Modelos principales:
  - Transformers diseñados para datos tabulares
  - Baseline: Random Forest
- Comparación de métricas de clasificación para determinar el método más efectivo.

## Notas de proyecto

- Este proyecto forma parte de mi maestría en ciencia de datos en la Universidad.
- Quiero mantener todo ordenado en distintos notebooks para que cada etapa del trabajo quede clara y reproducible.
- Debe existir un `README.md` donde se entienda la idea general del proyecto y lo que se hace en cada notebook.
- Mantener el `README.md` actualizado cada vez que se realizan cambios importantes.

## Uso esperado

Este archivo documenta el contexto del proyecto y los agentes de análisis para facilitar el trabajo colaborativo y el desarrollo del modelo.

## Política de reproducibilidad (obligatoria)

- Todas las notebooks deben crear automáticamente un directorio `results/<timestamp>/` con los artefactos de cada corrida: modelos, métricas, logs, figuras y un `manifest.json` con metadatos reproducibles (hash del dataset, commit git si aplica, timestamp UTC, y `random_state`).
- Antes de entrenar, fijar `random_state` y propagar la semilla a `numpy`, `random` y `torch` cuando corresponda.
- Guardar los requerimientos de Python en `requirements.txt` dentro del directorio de resultados usando `pip freeze` (o similar) para que las dependencias queden registradas.
- Los modelos deben guardarse en `results/<timestamp>/models/` y las métricas agregarse a `results/<timestamp>/metrics/metrics.csv` y `metrics.json`.
- Incluir instrucciones de cómo reproducir exactamente el experimento en `results/<timestamp>/README.md` si algún paso no es trivial.

Esta política debe respetarse en todas las notebooks del repositorio para asegurar trazabilidad y facilidad de publicación de resultados en el paper.

