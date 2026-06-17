# Sistema híbrido y explicable de recomendación de películas

Proyecto final del Curso de Especialización en Inteligencia Artificial y Big Data.

El objetivo del proyecto es construir un recomendador de películas que combine datos públicos de MovieLens con preferencias reales del usuario obtenidas desde Trakt, generando recomendaciones personalizadas, justificables y exportables a Power BI.

---

## 1. Resumen del proyecto

El sistema trabaja con un flujo completo de datos:

1. **Carga de datos**: lectura de los ficheros originales de MovieLens.
2. **Limpieza y transformación**: tratamiento de títulos, años, géneros, tags y métricas de popularidad.
3. **Análisis exploratorio**: revisión de distribución de películas, valoraciones, géneros y calidad del dataset.
4. **Integración con Trakt**: obtención de ratings y películas vistas del usuario mediante API.
5. **Preprocesado semántico**: preparación de tags y señales útiles para el recomendador.
6. **Recomendador híbrido final**: combinación de contenido, perfil de usuario, señal colaborativa, calidad, popularidad suavizada y diversidad.
7. **Visualización**: generación de datasets finales para Power BI.

El resultado final no se limita a devolver una lista de películas. También aporta información explicativa sobre por qué se recomienda cada título y permite analizar el comportamiento del recomendador mediante métricas y visualizaciones.

---

## 2. Estructura del repositorio

```text
TFG/
│
├── data/
│   ├── raw/                 # Datos originales de MovieLens incluidos para revisión/ejecución.
│   └── processed/           # Datos procesados generados por los notebooks.
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
│   └── figures/             # Figuras y previsualizaciones.
│
├── src/                     # Funciones reutilizables del proyecto.
│
├── .env.example             # Plantilla de variables de entorno para Trakt.
├── .gitignore
├── requirements.txt
└── README.md
```

---

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

---

## 4. Datos incluidos

El proyecto utiliza MovieLens 32M como fuente principal.

La carpeta `data/raw/` contiene los archivos originales necesarios para ejecutar el flujo principal:

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

La carpeta `data/processed/` contiene datos procesados generados por los notebooks. Se incluye para facilitar la revisión del proyecto y permitir ejecutar directamente las fases finales sin repetir todo el procesamiento desde cero.

También se incluyen los datasets finales utilizados por Power BI en:

```text
powerbi/datasets/
```

Los archivos principales de salida son:

```text
recomendaciones_finales.csv
perfil_usuario_trakt.csv
metricas_recomendador.csv
distribucion_recomendaciones.csv
```

---

## 5. Modos de ejecución

El proyecto puede utilizarse de tres formas.

---

### Modo A: ejecución completa desde cero

Este modo reproduce todo el flujo técnico del proyecto.

Pasos:

1. Comprobar que los CSV de MovieLens están en `data/raw/`.
2. Crear el entorno virtual.
3. Instalar las dependencias con `pip install -r requirements.txt`.
4. Configurar Trakt si se desea usar una cuenta real.
5. Abrir Jupyter Notebook o JupyterLab.
6. Ejecutar los notebooks del `01` al `06` en orden.
7. Revisar los CSV generados en `powerbi/datasets/`.
8. Abrir Power BI y actualizar el dashboard si es necesario.

Orden recomendado:

```text
notebooks/01_carga_datos.ipynb
notebooks/02_limpieza_transformacion.ipynb
notebooks/03_analisis_exploratorio.ipynb
notebooks/04_trakt_api_integracion.ipynb
notebooks/05_preprocesado_tags_semanticos.ipynb
notebooks/06_recomendador_hibrido_final.ipynb
```

El notebook `04_trakt_api_integracion.ipynb` requiere credenciales de Trakt si se desea repetir la integración con una cuenta real. Si no se dispone de credenciales, se pueden utilizar los ficheros ya generados en `data/processed/`.

---

### Modo B: ejecución offline directa para revisión

Este modo está pensado para revisión académica, defensa del proyecto o ejecución rápida en local/Codespaces.

No requiere conectarse a Trakt si se usan los archivos ya generados.

Pasos:

1. Clonar o descargar el repositorio.
2. Crear entorno virtual e instalar dependencias.
3. Comprobar que existen:
   - `data/raw/`
   - `data/processed/`
   - `powerbi/datasets/`
   - `notebooks/`
   - `powerbi/`
4. Abrir `notebooks/06_recomendador_hibrido_final.ipynb`.
5. Revisar la generación del ranking final.
6. Abrir los CSV finales en `powerbi/datasets/`.
7. Abrir el dashboard de Power BI si se desea revisar la visualización final.

En este modo se puede revisar el proyecto sin usar credenciales personales de Trakt. El notebook de Trakt queda documentado como parte del flujo, pero no es obligatorio reautenticar si los resultados ya han sido generados previamente.

---

### Modo C: ejecución en GitHub Codespaces

El repositorio está preparado para poder revisarse desde GitHub Codespaces.

Pasos recomendados:

1. Abrir el repositorio en GitHub.
2. Seleccionar `Code > Codespaces > Create codespace`.
3. Esperar a que se cargue el entorno.
4. Crear entorno virtual:

```bash
python -m venv .venv
```

5. Activarlo:

```bash
source .venv/bin/activate
```

6. Instalar dependencias:

```bash
pip install -r requirements.txt
```

#### Selección de kernel en Codespaces

Si el notebook no detecta automáticamente el entorno virtual, se puede registrar manualmente el kernel de Jupyter:

```bash
python -m pip install ipykernel jupyter notebook
python -m ipykernel install --user --name tfg-venv --display-name "TFG Python"
jupyter kernelspec list

7. Abrir Jupyter:

```bash
jupyter notebook
```

8. Ejecutar o revisar los notebooks en el orden indicado.

Para revisión rápida se recomienda abrir directamente:

```text
notebooks/06_recomendador_hibrido_final.ipynb
```

y comprobar los resultados ya generados en:

```text
powerbi/datasets/
```

---

## 6. Flujo principal de notebooks

El flujo final del proyecto está formado por estos notebooks:

```text
notebooks/01_carga_datos.ipynb
notebooks/02_limpieza_transformacion.ipynb
notebooks/03_analisis_exploratorio.ipynb
notebooks/04_trakt_api_integracion.ipynb
notebooks/05_preprocesado_tags_semanticos.ipynb
notebooks/06_recomendador_hibrido_final.ipynb
```

El recomendador final se encuentra en:

```text
notebooks/06_recomendador_hibrido_final.ipynb
```

Los notebooks de `archive/` y `experiments/` no forman parte de la ejecución final. Se conservan únicamente como trazabilidad del desarrollo.

---

## 7. Integración con Trakt

La integración con Trakt permite usar ratings y películas vistas reales del usuario.

Para ejecutarla con una cuenta propia se debe crear una aplicación en Trakt y configurar un archivo `.env` a partir de `.env.example`.

El archivo `.env.example` contiene la estructura esperada:

```env
TRAKT_CLIENT_ID=your_client_id_here
TRAKT_CLIENT_SECRET=your_client_secret_here
TRAKT_SCOPE=public
```

Pasos:

1. Copiar `.env.example` y renombrarlo a `.env`.
2. Sustituir `your_client_id_here` por el Client ID de la aplicación de Trakt.
3. Sustituir `your_client_secret_here` por el Client Secret de la aplicación de Trakt.
4. Ejecutar:

```text
notebooks/04_trakt_api_integracion.ipynb
```

5. Seguir el proceso de autenticación indicado por el notebook.

Los siguientes ficheros no deben subirse nunca al repositorio:

```text
.env
data/processed/trakt_token.json
trakt_token.json
```

---

## 8. Salidas finales para Power BI

El notebook final genera los datasets que alimentan el dashboard:

```text
powerbi/datasets/recomendaciones_finales.csv
powerbi/datasets/perfil_usuario_trakt.csv
powerbi/datasets/metricas_recomendador.csv
powerbi/datasets/distribucion_recomendaciones.csv
```

Estos ficheros se utilizan en el dashboard incluido en la carpeta `powerbi/`.

El dashboard permite revisar:

- Resumen general del recomendador.
- Perfil de usuario obtenido desde Trakt.
- Top recomendaciones.
- Explicabilidad del ranking.
- Diversidad por géneros, décadas, buckets y ramas.

---

## 9. Resultados finales del recomendador

La versión final del sistema genera:

```text
20 recomendaciones finales
4516 candidatos evaluados
187 ratings de Trakt mapeados
218 películas vistas mapeadas
Score mínimo: 0,6
Score máximo: 0,99
Score medio: 0,795
Riesgo medio de falso positivo: 0,2692
Margen positivo medio: 0,8982
5 buckets interpretables
5 ramas de recomendación
```

Los buckets utilizados son:

```text
Descubrimiento compatible
Título consolidado
Riesgo controlado
Apuesta segura
Muy parecida a favoritas
```

Las ramas obtenidas para el perfil analizado son:

```text
crime_thriller
emotional_character_drama
psychological_thriller
satire_surreal_comedy
sci_fi_reflective
```

Estas ramas corresponden al perfil concreto utilizado en el proyecto. Si se ejecuta el sistema con otro usuario de Trakt, las ramas podrían cambiar o tener distinto peso.

---

## 10. Notas de seguridad

- No se suben credenciales personales al repositorio.
- `.env` queda ignorado por Git.
- El token de Trakt no debe entregarse ni publicarse.
- Para una revisión offline basta con los CSV y ficheros procesados ya generados.
- Si se desea repetir la integración con Trakt, cada usuario debe configurar sus propias credenciales.

---

## 11. Estado de los experimentos

LightFM y otras variantes previas se conservan en `notebooks/experiments/`, pero no forman parte del sistema final.

El sistema final entregado corresponde al flujo principal:

```text
01_carga_datos
02_limpieza_transformacion
03_analisis_exploratorio
04_trakt_api_integracion
05_preprocesado_tags_semanticos
06_recomendador_hibrido_final
```

---

## 12. Autor

Álex Bustillo Echevarría  
Proyecto Final - Curso de Especialización en Inteligencia Artificial y Big Data  
Convocatoria 2S2526
