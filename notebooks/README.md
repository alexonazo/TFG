# Notebooks del proyecto

Esta carpeta contiene el flujo final de notebooks del TFG. Los notebooks están numerados en el orden en el que deben ejecutarse y representan el ciclo completo del proyecto: carga de datos, limpieza, análisis, integración con Trakt, preprocesado semántico y recomendador híbrido final.

## Flujo principal final

| Orden | Notebook | Función principal | Entrada esperada | Salida esperada |
|---:|---|---|---|---|
| 1 | `01_carga_datos.ipynb` | Cargar los ficheros originales de MovieLens y comprobar su estructura. | `data/raw/movies.csv`, `ratings.csv`, `tags.csv`, `links.csv` | DataFrames base cargados y revisión inicial de tamaño/columnas. |
| 2 | `02_limpieza_transformacion.ipynb` | Limpiar títulos, años, géneros, tags y preparar variables útiles. | Datos cargados desde MovieLens | Ficheros procesados en `data/processed/`. |
| 3 | `03_analisis_exploratorio.ipynb` | Analizar distribución de valoraciones, géneros, años, popularidad y calidad del dataset. | Datos limpios/procesados | Gráficos y conclusiones para memoria/presentación. |
| 4 | `04_trakt_api_integracion.ipynb` | Conectar con Trakt y obtener ratings y películas vistas del usuario. | `.env` con credenciales de Trakt y datos de MovieLens | Perfil real del usuario y datos mapeados con MovieLens. |
| 5 | `05_preprocesado_tags_semanticos.ipynb` | Preparar tags y señales semánticas para el recomendador. | Tags procesados y películas limpias | Variables semánticas listas para el recomendador final. |
| 6 | `06_recomendador_hibrido_final.ipynb` | Ejecutar el recomendador híbrido explicable y exportar resultados. | Datos procesados, perfil de usuario y señales semánticas | Recomendaciones finales y CSV de Power BI. |

El recomendador final está en:

```text
notebooks/06_recomendador_hibrido_final.ipynb
```

## Orden recomendado de ejecución

Desde la raíz del proyecto:

```bash
jupyter notebook
```

Después abrir y ejecutar en este orden:

```text
01_carga_datos.ipynb
02_limpieza_transformacion.ipynb
03_analisis_exploratorio.ipynb
04_trakt_api_integracion.ipynb
05_preprocesado_tags_semanticos.ipynb
06_recomendador_hibrido_final.ipynb
```

## Ejecución offline de notebooks

Para revisar el proyecto sin conexión a Internet, no es necesario volver a autenticar Trakt si la entrega incluye los ficheros ya generados.

En modo offline:

1. Revisar `01`, `02` y `03` para entender el tratamiento de MovieLens.
2. No ejecutar de nuevo las celdas de autenticación del notebook `04`, salvo que se tenga conexión y credenciales.
3. Usar los datos ya generados en `data/processed/`.
4. Ejecutar o revisar `06_recomendador_hibrido_final.ipynb` como notebook final.
5. Abrir los CSV finales de `powerbi/datasets/`.

Si se desea que el evaluador no tenga que repetir ningún procesamiento, entregar los notebooks con outputs ya generados y los CSV finales incluidos.

## Uso con Trakt propio

Para ejecutar el notebook `04` con una cuenta propia de Trakt:

1. Crear una aplicación de Trakt.
2. Copiar `.env.example` como `.env`.
3. Rellenar `TRAKT_CLIENT_ID` y `TRAKT_CLIENT_SECRET`.
4. Ejecutar `04_trakt_api_integracion.ipynb`.
5. Seguir las instrucciones de autenticación que aparezcan en pantalla.
6. Continuar con `05` y `06`.

## Notebooks experimentales

La carpeta `notebooks/experiments/` contiene aproximaciones alternativas que no forman parte del flujo principal:

- `experiments/04_recomendador_contenido.ipynb`
- `experiments/04b_recomendador_generos_tags.ipynb`
- `experiments/07_lightfm_hybrid_model.ipynb`

LightFM se conserva como experimento, pero no se considera el modelo final de entrega.

## Archivo histórico

La carpeta `notebooks/archive/` conserva versiones intermedias del desarrollo:

- `archive/04c_recomendador_avanzado.ipynb`
- `archive/04d_recomendador_perfil_usuario_explicable.ipynb`
- `archive/05_evaluacion_resultados.ipynb`
- `archive/06_export_powerbi.ipynb`

Estos notebooks no deben ejecutarse para reproducir la entrega final. Sirven para mostrar evolución y trazabilidad.

## Criterio de corrección

Para evaluar el proyecto se debe revisar especialmente:

- que el flujo final `01-06` se entiende y está documentado;
- que el notebook `06` genera recomendaciones explicables;
- que los resultados se exportan correctamente a Power BI;
- que no se usan credenciales personales dentro del código;
- que los experimentos están separados del flujo principal.
