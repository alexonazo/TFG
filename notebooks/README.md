# Notebooks del proyecto

Esta carpeta contiene el flujo final de notebooks del TFG con numeracion limpia 01-06. Los experimentos y notebooks historicos se conservan aparte para trazabilidad.

## Flujo principal final

1. `01_carga_datos.ipynb`
2. `02_limpieza_transformacion.ipynb`
3. `03_analisis_exploratorio.ipynb`
4. `04_trakt_api_integracion.ipynb`
5. `05_preprocesado_tags_semanticos.ipynb`
6. `06_recomendador_hibrido_final.ipynb`

El recomendador final esta en `notebooks/06_recomendador_hibrido_final.ipynb`.

## Orden recomendado de ejecucion

1. Ejecutar `01_carga_datos.ipynb` para preparar los datos base.
2. Ejecutar `02_limpieza_transformacion.ipynb` para generar datasets procesados.
3. Revisar `03_analisis_exploratorio.ipynb` para el analisis del dataset.
4. Ejecutar `04_trakt_api_integracion.ipynb` para integrar ratings y vistos de Trakt.
5. Ejecutar `05_preprocesado_tags_semanticos.ipynb` para preparar tags semanticos.
6. Ejecutar `06_recomendador_hibrido_final.ipynb` para generar las recomendaciones finales y sus exportaciones.

## Experimentos

La carpeta `notebooks/experiments/` contiene aproximaciones alternativas que no forman parte del flujo principal:

- `experiments/04_recomendador_contenido.ipynb`
- `experiments/04b_recomendador_generos_tags.ipynb`
- `experiments/07_lightfm_hybrid_model.ipynb`

LightFM esta en `notebooks/experiments/07_lightfm_hybrid_model.ipynb` y se considera experimental.

## Archivo historico

La carpeta `notebooks/archive/` conserva notebooks intermedios de evolucion del proyecto:

- `archive/04c_recomendador_avanzado.ipynb`
- `archive/04d_recomendador_perfil_usuario_explicable.ipynb`
- `archive/05_evaluacion_resultados.ipynb`
- `archive/06_export_powerbi.ipynb`

Estos notebooks no deben ejecutarse como parte del flujo principal salvo que se quiera revisar la evolucion historica del sistema.

## Notas

- El notebook 06 es el que genera las recomendaciones finales y las exportaciones asociadas.
- Power BI se exporta desde `06_recomendador_hibrido_final.ipynb` a `../powerbi/datasets/`.
- La entrega final de Power BI usa cuatro datasets: `recomendaciones_finales.csv`, `perfil_usuario_trakt.csv`, `metricas_recomendador.csv` y `distribucion_recomendaciones.csv`.
- No se han limpiado outputs ni cambiado datos o credenciales.
