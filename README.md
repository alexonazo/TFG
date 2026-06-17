# Sistema híbrido y explicable de recomendación de películas

Proyecto final del Curso de Especialización en Inteligencia Artificial y Big Data.

El objetivo del proyecto es construir un sistema híbrido y explicable de recomendación de películas que combine datos públicos de MovieLens con preferencias reales del usuario obtenidas desde Trakt, generando recomendaciones personalizadas, justificables y exportables a Power BI.

El proyecto recorre el ciclo completo del dato: carga, limpieza, análisis exploratorio, integración con API externa, preprocesado semántico, construcción del recomendador, evaluación interna y comunicación de resultados mediante un dashboard.

---

## 1. Aviso importante sobre las versiones de datos

Este proyecto se entrega en dos formatos complementarios:

### Versión completa de entrega en Google Drive

La carpeta de entrega en Google Drive contiene la versión completa del proyecto, incluyendo los datos completos de MovieLens 32M y los artefactos finales generados.

Esta versión es la que debe utilizarse para revisar el proyecto completo y reproducir los resultados finales presentados en la memoria, la presentación y el vídeo de defensa.

En la carpeta de código del Drive se incluye:

```text
data/raw/          # Versión completa de MovieLens 32M
data/processed/    # Datos procesados generados durante el proyecto
powerbi/datasets/  # CSV finales utilizados por Power BI
notebooks/         # Notebooks del flujo principal
src/               # Funciones reutilizables
powerbi/           # Dashboard y archivos relacionados
reports/           # Gráficos, resultados y figuras
```

### Versión de GitHub

El repositorio de GitHub incluye una versión más ligera del proyecto, preparada para revisión rápida, navegación del código y ejecución en entornos como GitHub Codespaces.

En GitHub puede incluirse una versión reducida o de muestra de los datos para evitar problemas de tamaño, tiempos de carga o límites del repositorio. Esta versión permite comprobar la estructura, ejecutar el flujo y revisar el funcionamiento general, pero no debe interpretarse como la fuente principal para reproducir exactamente todas las métricas finales.

Por tanto:

```text
Google Drive  → versión completa de entrega, con MovieLens 32M completo.
GitHub        → versión ligera/reducida para revisión rápida y Codespaces.
```

Los resultados finales indicados en la memoria, la presentación y Power BI corresponden a la ejecución completa del proyecto con los datos preparados para la entrega.

---

## 2. Resumen del proyecto

El sistema trabaja con un flujo completo de datos:

1. **Carga de datos**: lectura de los ficheros originales de MovieLens.
2. **Limpieza y transformación**: tratamiento de títulos, años, géneros, tags y métricas de popularidad.
3. **Análisis exploratorio**: revisión de distribución de películas, valoraciones, géneros, décadas y calidad del dataset.
4. **Integración con Trakt**: obtención de ratings y películas vistas del usuario mediante API.
5. **Preprocesado semántico**: limpieza, normalización y preparación de tags para enriquecer la señal de contenido.
6. **Recomendador híbrido final**: combinación de contenido, perfil de usuario, señal colaborativa item-item, calidad, popularidad suavizada, riesgo y diversidad.
7. **Exportación de resultados**: generación de CSV finales para Power BI.
8. **Visualización**: construcción de un dashboard final para comunicar el perfil, las recomendaciones, la explicabilidad y la diversidad.

El resultado final no se limita a devolver una lista de películas. Cada recomendación incorpora información adicional como score, bucket, rama de recomendación, señal dominante, riesgo de falso positivo, margen positivo y explicación textual.

---

## 3. Estructura del repositorio

```text
TFG/
│
├── data/
│   ├── raw/                 
│   │   └── Datos originales de MovieLens.
│   │       En Drive se incluye la versión completa.
│   │       En GitHub puede incluirse una versión reducida para ejecución rápida.
│   │
│   └── processed/           
│       └── Datos procesados generados por los notebooks.
│
├── notebooks/
│   ├── 01_carga_datos.ipynb
│   ├── 02_limpieza_transformacion.ipynb
│   ├── 03_analisis_exploratorio.ipynb
│   ├── 04_trakt_api_integracion.ipynb
│   ├── 05_preprocesado_tags_semanticos.ipynb
│   ├── 06_recomendador_hibrido_final.ipynb
│   ├── archive/
│   │   └── Notebooks históricos fuera del flujo final.
│   └── experiments/
│       └── Experimentos que no forman parte de la entrega final.
│
├── powerbi/
│   ├── datasets/
│   │   └── CSV finales utilizados por Power BI.
│   ├── recomendador_peliculas_dashboard.pbip
│   ├── recomendador_peliculas_dashboard.Report/
│   └── recomendador_peliculas_dashboard.SemanticModel/
│
├── reports/
│   ├── graficos/
│   │   └── Gráficos generados para memoria y presentación.
│   ├── resultados/
│   │   └── Tablas y resultados exportados.
│   └── figures/
│       └── Figuras y previsualizaciones.
│
├── src/
│   └── Funciones reutilizables del proyecto.
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 4. Requisitos previos

### Software recomendado

- Python 3.10 o superior.
- Jupyter Notebook o JupyterLab.
- Git, si se va a clonar el repositorio.
- Power BI Desktop, si se desea abrir o modificar el dashboard.
- Cuenta de Trakt, solo si se desea ejecutar la integración con datos personales reales.

### Librerías principales

Las dependencias del proyecto están recogidas en `requirements.txt`.

Entre las librerías utilizadas se encuentran:

```text
pandas
numpy
scikit-learn
scipy
matplotlib
jupyter
notebook
ipykernel
deep-translator
python-dotenv
requests
```

Estas librerías cubren la carga y tratamiento de datos, el análisis exploratorio, el cálculo de similitudes, el manejo de matrices dispersas, la ejecución de notebooks, la integración con Trakt, la lectura de variables de entorno y la exportación de resultados.

---

## 5. Instalación del entorno

Desde la raíz del proyecto:

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En macOS/Linux o Codespaces:

```bash
source .venv/bin/activate
```

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

python -m pip install ipykernel jupyter notebook
python -m ipykernel install --user --name tfg-venv --display-name "TFG Python"
jupyter kernelspec list

Reiniciar la ventana y seleccionar el Kernel

Para abrir Jupyter Notebook:

```bash
jupyter notebook
```

---

## 6. Datos necesarios

El proyecto utiliza MovieLens como fuente principal.

Los archivos esperados en `data/raw/` son:

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

### Versión completa

La versión completa de estos archivos se encuentra en la carpeta de código entregada en Google Drive.

Esta versión corresponde a MovieLens 32M y permite reproducir el flujo completo del proyecto.

### Versión reducida en GitHub

El repositorio de GitHub puede contener una versión reducida de estos datos para permitir una revisión más rápida y facilitar la ejecución en Codespaces.

Esta versión reducida sirve para comprobar el funcionamiento del pipeline, pero puede generar resultados distintos a los obtenidos con la versión completa.

---

## 7. Modos de ejecución

El proyecto puede revisarse o ejecutarse de varias formas.

---

### Modo A: revisión completa desde la carpeta de Drive

Este es el modo recomendado para la corrección final del proyecto.

La carpeta de Drive contiene la versión completa de datos y artefactos finales, por lo que permite revisar el proyecto tal como se ha presentado en la memoria, la presentación y el vídeo.

Pasos recomendados:

1. Descargar o abrir la carpeta de código entregada en Drive.
2. Comprobar que existen las carpetas:

```text
data/raw/
data/processed/
notebooks/
src/
powerbi/
powerbi/datasets/
reports/
```

3. Crear y activar el entorno virtual.
4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

5. Abrir Jupyter Notebook.
6. Revisar o ejecutar los notebooks en orden.
7. Abrir los CSV finales en `powerbi/datasets/`.
8. Abrir el dashboard de Power BI desde la carpeta `powerbi/`.

Este modo es el más adecuado para verificar los resultados finales del proyecto.

---

### Modo B: ejecución completa desde cero

Este modo reproduce todo el flujo técnico del proyecto.

Pasos:

1. Comprobar que los CSV de MovieLens están en `data/raw/`.
2. Crear el entorno virtual.
3. Instalar las dependencias.
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

El notebook `04_trakt_api_integracion.ipynb` requiere credenciales de Trakt si se desea repetir la integración con una cuenta real.

Si no se dispone de credenciales, se pueden utilizar los archivos ya generados en `data/processed/`.

---

### Modo C: revisión rápida desde GitHub o Codespaces

Este modo está pensado para revisar el proyecto sin descargar manualmente toda la entrega.

El repositorio de GitHub permite revisar:

- La estructura del proyecto.
- Los notebooks principales.
- El código reutilizable en `src/`.
- El README.
- Los datasets reducidos o de muestra, si están incluidos.
- Los CSV finales disponibles.
- La lógica general del recomendador.

En GitHub Codespaces:

1. Abrir el repositorio en GitHub.
2. Seleccionar:

```text
Code > Codespaces > Create codespace
```

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

7. Abrir Jupyter:

```bash
jupyter notebook
```

8. Ejecutar o revisar los notebooks.

Para una revisión rápida se recomienda abrir directamente:

```text
notebooks/06_recomendador_hibrido_final.ipynb
```

y comprobar los resultados disponibles en:

```text
powerbi/datasets/
```

Importante: la versión de GitHub puede trabajar con datos reducidos, por lo que las métricas pueden no coincidir exactamente con las de la versión completa entregada en Drive.

---

### Modo D: revisión offline sin Trakt

Este modo permite revisar el proyecto sin conectarse a la API de Trakt.

Se puede utilizar cuando ya existen archivos generados en:

```text
data/processed/
powerbi/datasets/
```

Pasos:

1. Clonar o descargar el proyecto.
2. Instalar dependencias.
3. Abrir los notebooks.
4. Revisar las salidas ya generadas.
5. Abrir `notebooks/06_recomendador_hibrido_final.ipynb`.
6. Abrir los CSV finales.
7. Abrir Power BI.

En este modo no hace falta autenticarse en Trakt, ya que se utilizan datos previamente procesados.

---

## 8. Flujo principal de notebooks

El flujo final del proyecto está formado por estos notebooks:

```text
01_carga_datos.ipynb
02_limpieza_transformacion.ipynb
03_analisis_exploratorio.ipynb
04_trakt_api_integracion.ipynb
05_preprocesado_tags_semanticos.ipynb
06_recomendador_hibrido_final.ipynb
```

### 01_carga_datos.ipynb

Carga los archivos originales de MovieLens y comprueba estructura, columnas y tamaño inicial de los datos.

### 02_limpieza_transformacion.ipynb

Limpia títulos, extrae años, trata géneros, calcula métricas agregadas y genera tablas procesadas.

### 03_analisis_exploratorio.ipynb

Analiza la distribución de películas, valoraciones, géneros, años, décadas y calidad general del dataset.

### 04_trakt_api_integracion.ipynb

Integra Trakt para obtener ratings reales y películas vistas del usuario. También realiza el mapeo con MovieLens mediante identificadores externos.

### 05_preprocesado_tags_semanticos.ipynb

Limpia, normaliza y prepara tags semánticos para enriquecer la señal de contenido del recomendador.

### 06_recomendador_hibrido_final.ipynb

Construye el recomendador híbrido final, calcula el ranking, genera explicaciones y exporta los datasets finales para Power BI.

El recomendador final se encuentra en:

```text
notebooks/06_recomendador_hibrido_final.ipynb
```

Los notebooks de `archive/` y `experiments/` no forman parte de la ejecución final. Se conservan únicamente como trazabilidad del desarrollo.

---

## 9. Integración con Trakt

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

Por seguridad, el proyecto puede revisarse sin volver a autenticar en Trakt si ya están disponibles los archivos procesados.

---

## 10. Salidas finales para Power BI

El notebook final genera los datasets que alimentan el dashboard:

```text
powerbi/datasets/recomendaciones_finales.csv
powerbi/datasets/perfil_usuario_trakt.csv
powerbi/datasets/metricas_recomendador.csv
powerbi/datasets/distribucion_recomendaciones.csv
```

Estos archivos permiten construir y actualizar el dashboard de Power BI.

El dashboard permite revisar:

- Resumen general del recomendador.
- Perfil de usuario obtenido desde Trakt.
- Ranking final de recomendaciones.
- Explicabilidad de cada recomendación.
- Diversidad por géneros, décadas, buckets y ramas.

---

## 11. Resultados finales del recomendador

La versión final del sistema, ejecutada con los datos completos preparados para la entrega, genera:

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

## 12. Notas sobre rendimiento

MovieLens 32M es un dataset grande. Algunas fases pueden tardar varios minutos, especialmente:

- Carga de ratings completos.
- Preprocesado semántico de tags.
- Construcción de matrices o señales colaborativas.
- Generación completa del recomendador final.

En entornos con recursos limitados, como Codespaces gratuito o máquinas con poca memoria, puede ser recomendable usar la versión reducida del repositorio de GitHub o revisar directamente los archivos procesados incluidos en la entrega.

La ejecución completa con los datos completos debe realizarse preferiblemente desde la carpeta de Drive descargada en un entorno local con suficiente memoria.

---

## 13. Solución de problemas comunes

### Jupyter no detecta el kernel del entorno virtual

En algunos entornos, especialmente en VS Code o GitHub Codespaces, puede ocurrir que el notebook no detecte automáticamente el entorno virtual.

En ese caso, desde la raíz del proyecto:

```bash
source .venv/bin/activate
python -m pip install ipykernel jupyter notebook
python -m ipykernel install --user --name tfg-venv --display-name "TFG Python"
jupyter kernelspec list
```

Después, en el notebook, seleccionar el kernel:

```text
TFG Python
```

o el intérprete asociado al entorno virtual:

```text
.venv/bin/python
```

Si VS Code no muestra el nuevo kernel, recargar la ventana:

```text
Ctrl + Shift + P → Developer: Reload Window
```

### Error por archivo no encontrado

Si aparece un error del tipo:

```text
FileNotFoundError: No se encontró el archivo esperado
```

comprobar que se está ejecutando el notebook desde la raíz del proyecto y que existen las carpetas:

```text
data/raw/
data/processed/
powerbi/datasets/
```

También conviene comprobar que los archivos tienen exactamente los nombres esperados:

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

### El notebook tarda demasiado

Algunas fases trabajan con muchos datos. Si se está usando Codespaces o una máquina limitada, se recomienda revisar directamente los datos procesados o ejecutar solo el notebook final con los archivos ya generados.

---

## 14. Notas de seguridad

- No se suben credenciales personales al repositorio.
- `.env` queda ignorado por Git.
- El token de Trakt no debe publicarse ni entregarse como parte pública del proyecto.
- Para una revisión offline basta con los CSV y ficheros procesados ya generados.
- Si se desea repetir la integración con Trakt, cada usuario debe configurar sus propias credenciales.
- Los archivos sensibles no deben mostrarse durante la defensa en vídeo.

---

## 15. Estado de los experimentos

LightFM y otras variantes previas se conservan en:

```text
notebooks/experiments/
```

Estos experimentos no forman parte del sistema final.

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

## 16. Recomendación para el evaluador

Para revisar el proyecto de forma rápida:

1. Leer este README.
2. Revisar la estructura del repositorio.
3. Abrir el notebook final:

```text
notebooks/06_recomendador_hibrido_final.ipynb
```

4. Revisar los CSV de salida:

```text
powerbi/datasets/
```

5. Abrir el dashboard de Power BI.
6. Consultar la memoria escrita para la explicación completa de metodología, análisis, diseño, pruebas y conclusiones.

Para reproducir los resultados completos, utilizar preferiblemente la carpeta de código incluida en Drive, ya que contiene la versión completa de MovieLens 32M.

---

## 17. Autor

Álex Bustillo Echevarría  
Proyecto Final - Curso de Especialización en Inteligencia Artificial y Big Data  
Convocatoria 2S2526
