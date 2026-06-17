# Sistema híbrido y explicable de recomendación de películas

Proyecto final del Curso de Especialización en Inteligencia Artificial y Big Data. El objetivo del proyecto es construir un recomendador de películas que combine datos públicos de MovieLens con preferencias reales del usuario obtenidas desde Trakt, generando recomendaciones justificables y exportables a Power BI.

## 1. Resumen del proyecto

El sistema trabaja con un flujo de datos completo:

1. **Carga de datos**: lectura de los ficheros originales de MovieLens.
2. **Limpieza y transformación**: tratamiento de títulos, años, géneros, tags y métricas de popularidad.
3. **Análisis exploratorio**: revisión de distribución de películas, valoraciones, géneros y calidad del dataset.
4. **Integración con Trakt**: obtención de ratings y películas vistas del usuario mediante API.
5. **Preprocesado semántico**: preparación de tags y señales útiles para el recomendador.
6. **Recomendador híbrido final**: combinación de contenido, perfil de usuario, señal colaborativa y reglas de diversidad.
7. **Visualización**: generación de datasets finales para Power BI.

El resultado final no se limita a devolver una lista de películas. También aporta información explicativa sobre por qué se recomienda cada título y permite analizar el comportamiento del recomendador mediante métricas y visualizaciones.

## 2. Estructura del repositorio

```text
TFG/
│
├── data/
│   ├── raw/                 # Datos originales de MovieLens. No se suben a GitHub.
│   └── processed/           # Datos procesados generados por los notebooks. No se suben a GitHub.
│
├── notebooks/
│   ├── 01_carga_datos.ipynb
│   ├── 02_limpieza_transformacion.ipynb
│   ├── 03_analisis_exploratorio.ipynb
│   ├── 04_trakt_api_integracion.ipynb
│   ├── 05_preprocesado_tags_semanticos.ipynb
│   ├── 06_recomendador_hibrido_final.ipynb
│   ├── archive/             # Notebooks históricos fuera del flujo final.
│   └── experiments/         # Experimentos que no forman parte de la entrega final.
│
├── powerbi/
│   ├── datasets/            # CSV finales para Power BI.
│   ├── recomendador_peliculas_dashboard.pbip
│   ├── recomendador_peliculas_dashboard.Report/
│   └── recomendador_peliculas_dashboard.SemanticModel/
│
├── reports/
│   ├── graficos/            # Gráficos generados para memoria y presentación.
│   ├── resultados/          # Tablas y resultados exportados.
│   └── figures/ powerbi_preview/
│
├── src/                     # Funciones reutilizables del proyecto.
│
├── .env.example             # Plantilla de variables de entorno para Trakt.
├── .gitignore
├── requirements.txt
└── README.md
```

## 3. Requisitos previos

### Software recomendado

- Python 3.10 o superior.
- Jupyter Notebook o JupyterLab.
- Git, si se va a clonar el repositorio.
- Power BI Desktop, si se desea abrir o modificar el dashboard.
- Cuenta de Trakt, solo si se desea ejecutar la integración con datos personales reales.

### Dependencias de Python

Desde la raíz del proyecto:

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En macOS/Linux:

```bash
source .venv/bin/activate
```

Instalación de librerías:

```bash
pip install -r requirements.txt
```

## 4. Datos necesarios

El proyecto utiliza MovieLens como fuente principal. Los datos originales no se suben al repositorio para evitar incluir ficheros pesados, pero deben colocarse en:

```text
data/raw/
```

La carpeta `data/raw/` debe contener, como mínimo:

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

La carpeta `data/processed/` se genera al ejecutar los notebooks. Para la entrega final en Drive puede incluirse ya preparada, de forma que el evaluador pueda revisar el proyecto sin repetir todo el procesamiento.

## 5. Modos de ejecución

El proyecto se puede utilizar de dos formas.

### Modo A: ejecución completa desde cero

# Datos brutos => data/raw

Esta carpeta debe contener los archivos originales del dataset MovieLens 32M:

- movies.csv
- ratings.csv
- tags.csv
- links.csv

Por tamaño, estos archivos no se incluyen en GitHub.  
Para reproducir el proyecto deben descargarse desde la página oficial de GroupLens:

MovieLens 32M Dataset:
https://grouplens.org/datasets/movielens/32m/

Una vez descargado el ZIP, deben copiarse los cuatro CSV anteriores dentro de esta carpeta.

Este modo reproduce todo el flujo técnico del proyecto.

1. Colocar los CSV de MovieLens en `data/raw/`.
2. Crear el entorno virtual e instalar dependencias.
3. Configurar Trakt si se desea usar datos reales del usuario.
4. Abrir Jupyter.
5. Ejecutar los notebooks del `01` al `06` en orden (El 04 no es necesario si no se tiene una cuenta de trakt, los archivos de un perfil de ejemplo están disponibles en data/processed).
6. Revisar los CSV generados en `powerbi/datasets/`.
7. Abrir Power BI y actualizar el dashboard.

### Modo B: ejecución offline directa para revisión

Este modo está pensado para la entrega final y para la corrección del proyecto. No requiere conectarse a Trakt ni volver a descargar datos, siempre que la carpeta entregada incluya los datos ya generados.

1. Descomprimir la carpeta final del proyecto.
2. Comprobar que existen:
   - `data/raw/` con los CSV originales de MovieLens;
   - `data/processed/` con los ficheros procesados;
   - `powerbi/datasets/` con los CSV finales;
   - `notebooks/` con los notebooks ejecutados;
   - `powerbi/` con el dashboard.
3. Crear entorno virtual e instalar dependencias si se quieren abrir o reejecutar notebooks.
4. Abrir `notebooks/06_recomendador_hibrido_final.ipynb` para revisar el resultado final.
5. Abrir el dashboard de Power BI usando los CSV ya generados.

En este modo se puede revisar el proyecto sin usar credenciales personales de Trakt. El notebook de Trakt queda documentado como parte del flujo, pero no es obligatorio reautenticar si los resultados ya han sido generados previamente.

## 6. Flujo principal de notebooks

El flujo final del proyecto está formado por estos notebooks:

1. `notebooks/01_carga_datos.ipynb`
2. `notebooks/02_limpieza_transformacion.ipynb`
3. `notebooks/03_analisis_exploratorio.ipynb`
4. `notebooks/04_trakt_api_integracion.ipynb`
5. `notebooks/05_preprocesado_tags_semanticos.ipynb`
6. `notebooks/06_recomendador_hibrido_final.ipynb`

El recomendador final se encuentra en:

```text
notebooks/06_recomendador_hibrido_final.ipynb
```

Los notebooks de `archive/` y `experiments/` no forman parte de la ejecución final. Se conservan únicamente como trazabilidad del desarrollo.

## 7. Integración con Trakt

La integración con Trakt permite usar ratings y películas vistas reales del usuario. Para ello se debe crear una aplicación en Trakt y configurar un archivo `.env` a partir de `.env.example`.

El archivo `.env.example` contiene la estructura esperada:

```env
TRAKT_CLIENT_ID=your_client_id_here
TRAKT_CLIENT_SECRET=your_client_secret_here
TRAKT_SCOPE=public
```

Para configurar las credenciales:

1. Copiar `.env.example` y renombrarlo a `.env`.
2. Sustituir `your_client_id_here` por el Client ID de la aplicación de Trakt.
3. Sustituir `your_client_secret_here` por el Client Secret de la aplicación de Trakt.
4. Ejecutar `notebooks/04_trakt_api_integracion.ipynb`.
5. Seguir el proceso de autenticación que indique el notebook.

Los siguientes ficheros no deben subirse nunca al repositorio:

```text
.env
data/processed/trakt_token.json
```

## 8. Salidas finales para Power BI

El notebook final genera los datasets que alimentan el dashboard:

```text
powerbi/datasets/recomendaciones_finales.csv
powerbi/datasets/perfil_usuario_trakt.csv
powerbi/datasets/metricas_recomendador.csv
powerbi/datasets/distribucion_recomendaciones.csv
```

Estos ficheros se pueden abrir directamente desde Power BI Desktop o desde el proyecto `.pbip` incluido en la carpeta de Drive dentro de PowerBi.

## 9. Notas de seguridad

- No se suben credenciales personales al repositorio.
- `.env` queda ignorado por Git.
- El token de Trakt no debe entregarse salvo que se quiera reproducir exactamente la sesión del autor en un entorno controlado.
- Para una revisión offline basta con entregar los CSV finales ya generados.

## 10. Estado de los experimentos

LightFM y otras variantes previas se conservan en `notebooks/experiments/`, pero no forman parte del sistema final. El sistema final entregado corresponde al flujo principal `01-06`.
