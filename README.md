# TFG Recomendador de Peliculas

Proyecto de TFG de IA y Big Data sobre un recomendador de peliculas explicable e hibrido usando MovieLens como base y Trakt como fuente de datos reales del usuario.

## Objetivo actual

El objetivo del proyecto es construir un recomendador explicable que combine:

- MovieLens como dataset principal;
- perfiles de usuario basados en generos y tags;
- ratings y peliculas vistas reales obtenidas desde Trakt;
- senales colaborativas item-item como parte del recomendador hibrido;
- un score final hibrido que sea facil de justificar.

## Arquitectura actual

La estructura del proyecto se organiza en tres capas:

1. Preparacion de datos.
2. Integracion con Trakt y enriquecimiento semantico.
3. Recomendador hibrido final explicable.

## Flujo de notebooks

### Flujo principal

El orden recomendado de ejecucion es:

1. `notebooks/01_carga_datos.ipynb`
2. `notebooks/02_limpieza_transformacion.ipynb`
3. `notebooks/03_analisis_exploratorio.ipynb`
4. `notebooks/04_trakt_api_integracion.ipynb`
5. `notebooks/05_preprocesado_tags_semanticos.ipynb`
6. `notebooks/06_recomendador_hibrido_final.ipynb`

El recomendador final es `notebooks/06_recomendador_hibrido_final.ipynb`.

### Notebooks secundarios

Estos notebooks se conservan como archivo historico, pero no forman parte del flujo principal:

- `notebooks/archive/04c_recomendador_avanzado.ipynb`
- `notebooks/archive/04d_recomendador_perfil_usuario_explicable.ipynb`
- `notebooks/archive/05_evaluacion_resultados.ipynb`
- `notebooks/archive/06_export_powerbi.ipynb`

### Experimentos

Las versiones previas del recomendador se han movido a:

- `notebooks/experiments/04_recomendador_contenido.ipynb`
- `notebooks/experiments/04b_recomendador_generos_tags.ipynb`
- `notebooks/experiments/07_lightfm_hybrid_model.ipynb`

LightFM queda como experimento y no forma parte del recomendador final.

## Integracion con Trakt

El proyecto ya incluye una integracion funcional con Trakt para:

- autenticar el usuario con device flow;
- descargar ratings reales;
- descargar peliculas vistas;
- mapear esos datos con MovieLens mediante `links.csv`;
- preparar un perfil compatible con el recomendador explicable.

Los ficheros sensibles no deben subirse al repositorio:

- `.env`
- `data/processed/trakt_token.json`

## Instalacion

Crear un entorno virtual e instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecucion

La forma recomendada de trabajar es abrir los notebooks en orden, empezando por la carga y limpieza de datos. El flujo principal deja preparados:

- `movies_clean.csv`
- tags traducidos y normalizados
- integracion con Trakt
- tags semanticos preprocesados
- recomendador hibrido final

## Estructura de carpetas

- `data/raw/`: datos originales.
- `data/processed/`: datos limpios y ficheros intermedios.
- `notebooks/`: flujo principal del proyecto.
- `notebooks/experiments/`: versiones previas o experimentales.
- `notebooks/archive/`: evolucion historica fuera del flujo principal.
- `src/`: funciones reutilizables.
- `reports/resultados/`: tablas y resultados exportados.
- `reports/graficos/`: graficos para la memoria.
- `powerbi/`: datasets preparados para Power BI.

## Posible refactorizacion futura

En la siguiente fase del proyecto se moveran funciones comunes a:

- `src/trakt_utils.py`
- `src/profile_recommender.py`
- `src/hybrid_recommender.py`

La version final actual ya concentra el flujo de recomendacion en `notebooks/06_recomendador_hibrido_final.ipynb`; cualquier ampliacion futura debe mantenerse fuera del flujo principal hasta estar validada.
