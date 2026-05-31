# Proyecto de titulación - Clasificación de eventos sísmicos en Cotopaxi

Este proyecto es parte de mi maestría en ciencia de datos en la Universidad. El objetivo es aplicar transformers a datos tabulares y comparar su desempeño con un baseline de Random Forest usando eventos sísmicos del volcán Cotopaxi.

## Descripción general

- Dataset: eventos sísmicos del volcán Cotopaxi.
- Variable objetivo: `type` (tipo de evento sísmico).
  - Ejemplos: `VT` (Volcano-Tectonic), `LP` (Long-Period), entre otros.
- Tipos de variables:
  - Temporales: prefijo `t_`
  - Frecuenciales: prefijo `f_`
  - Wavelet: prefijo `w_`

## Enfoque de modelado

- Modelos principales:
  - Transformers para datos tabulares.
  - Baseline: Random Forest.
- Se compararán métricas de clasificación para evaluar el desempeño.

## Organización del proyecto

- Cada notebook contendrá una parte específica del proceso: exploración de datos, preprocesamiento, entrenamiento y evaluación.
- El proyecto se mantendrá ordenado y documentado en distintos notebooks para facilitar la revisión y el análisis.

## Actualización de la documentación

- Este `README.md` debe mantenerse actualizado cada vez que se realicen cambios importantes en el proyecto.
- Las notas en `agentes.md` y los notebooks deben reflejar las decisiones principales y el estado actual del trabajo.

## Reproducibilidad de experimentos

Este repositorio registra y preserva resultados de entrenamiento en una estructura `results/<timestamp>/` creada automáticamente por las notebooks. Cada ejecución crea un directorio con:

- `models/` — modelos guardados (Pickle, zip, etc.)
- `metrics/` — `metrics.csv` y `metrics.json` con métricas por experimento
- `logs/` — salidas verbose y logs de entrenamiento
- `figures/` — figuras y curvas (confusion matrix, ROC, loss/metric per epoch)
- `reports/` — resúmenes y tablas listas para el paper
- `manifest.json` — metadatos esenciales: hash del dataset, commit git (si disponible), timestamp UTC y `random_state`

Para reproducir exactamente un experimento, carga el commit indicado en `manifest.json`, instala las dependencias listadas en `requirements.txt` dentro del mismo directorio `results/<timestamp>/`, y ejecuta la notebook con el mismo `random_state`.

