# Notebooks del proyecto

Esta carpeta separa el flujo principal final de los experimentos y del archivo historico. No se han borrado notebooks: los que ya no forman parte del flujo recomendado se conservan para trazabilidad.

## Flujo principal final

Estos notebooks forman la ruta principal del proyecto y son los que deben presentarse como flujo final:

1. `01_carga_datos.ipynb`
2. `02_limpieza_transformacion.ipynb`
3. `03_analisis_exploratorio.ipynb`
4. `06_trakt_api_integracion.ipynb`
5. `09_preprocesado_tags_semanticos.ipynb`
6. `08_recomendador_hibrido_final.ipynb`

El recomendador final del proyecto es `08_recomendador_hibrido_final.ipynb`.

## Orden recomendado de ejecucion

1. Ejecutar `01_carga_datos.ipynb` para preparar los datos base.
2. Ejecutar `02_limpieza_transformacion.ipynb` para generar datasets procesados.
3. Revisar `03_analisis_exploratorio.ipynb` para el analisis del dataset.
4. Ejecutar `06_trakt_api_integracion.ipynb` para integrar ratings y vistos de Trakt.
5. Ejecutar `09_preprocesado_tags_semanticos.ipynb` para preparar tags semanticos.
6. Ejecutar `08_recomendador_hibrido_final.ipynb` para obtener el ranking final y el debug snapshot.

## Experimentos

La carpeta `notebooks/experiments/` contiene aproximaciones alternativas o pruebas que no forman parte del flujo principal:

- `experiments/04_recomendador_contenido.ipynb`
- `experiments/04b_recomendador_generos_tags.ipynb`
- `experiments/07_lightfm_hybrid_model.ipynb`

`07_lightfm_hybrid_model.ipynb` queda documentado como experimento. LightFM no forma parte del recomendador final.

## Archivo historico

La carpeta `notebooks/archive/` conserva notebooks de evolucion del proyecto que ya no forman parte del flujo recomendado:

- `archive/04c_recomendador_avanzado.ipynb`
- `archive/04d_recomendador_perfil_usuario_explicable.ipynb`
- `archive/05_evaluacion_resultados.ipynb`
- `archive/06_export_powerbi.ipynb`

Estos notebooks se mantienen para consulta y trazabilidad historica. No deben ejecutarse como parte del flujo principal salvo que se quiera revisar la evolucion del sistema.

## Notas

- No se han limpiado outputs.
- No se han cambiado datos ni credenciales.
- No se ha modificado la logica interna de los notebooks.
- Con `EXPORT_FULL_RESULTS = False`, el flujo final solo debe generar el debug snapshot compacto cuando corresponda.
