# Notebooks del proyecto

## Flujo principal

Estos notebooks forman la ruta recomendada del proyecto:

1. `01_carga_datos.ipynb`
2. `02_limpieza_transformacion.ipynb`
3. `03_analisis_exploratorio.ipynb`
4. `04c_recomendador_avanzado.ipynb`
5. `04d_recomendador_perfil_usuario_explicable.ipynb`
6. `06_trakt_api_integracion.ipynb`

## Notebooks secundarios

Estos notebooks siguen disponibles, pero se consideran auxiliares o de apoyo:

- `05_evaluacion_resultados.ipynb`
- `06_export_powerbi.ipynb`

## Experimentos

La carpeta `notebooks/experiments/` guarda versiones previas o alternativas del sistema:

- `04_recomendador_contenido.ipynb`
- `04b_recomendador_generos_tags.ipynb`

## Orden recomendado de ejecucion

1. Cargar y preparar los datos.
2. Explorar el dataset.
3. Ejecutar el recomendador avanzado.
4. Ejecutar el recomendador por perfil de usuario.
5. Conectar Trakt y mapear los ratings reales a MovieLens.
6. Revisar evaluacion y exportacion a Power BI si hace falta.

## Notas

- El modelo colaborativo KNN aun no se ha incorporado.
- Los notebooks experimentales no forman parte del flujo principal de la memoria.
