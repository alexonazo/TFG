# Guía de ejecución del proyecto

Esta guía explica cómo ejecutar el proyecto completo, cómo revisarlo en modo offline y cómo configurar Trakt para utilizar datos reales de una cuenta personal.

## 1. Estructura

Antes de ejecutar el proyecto, la carpeta debe tener esta estructura:

```text
TFG/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── powerbi/
├── reports/
├── src/
├── .env.example
├── requirements.txt
└── README.md
```

## 2. Instalación del entorno

Desde la raíz del proyecto:

```bash
python -m venv .venv
```

Activar el entorno.

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Abrir Jupyter:

```bash
jupyter notebook
```

## 3. Preparación de datos MovieLens

Colocar los ficheros originales de MovieLens en:

```text
data/raw/
```

Ficheros necesarios:

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

## 4. Ejecución completa desde cero

Ejecutar los notebooks en este orden:

```text
notebooks/01_carga_datos.ipynb
notebooks/02_limpieza_transformacion.ipynb
notebooks/03_analisis_exploratorio.ipynb
notebooks/04_trakt_api_integracion.ipynb
notebooks/05_preprocesado_tags_semanticos.ipynb
notebooks/06_recomendador_hibrido_final.ipynb
```

### Qué hace cada fase

**01 - Carga de datos**

Carga los CSV originales de MovieLens y comprueba que tienen el formato correcto.

**02 - Limpieza y transformación**

Limpia títulos, años, géneros y tags. Genera datos preparados para el análisis y el recomendador.

**03 - Análisis exploratorio**

Analiza la calidad del dataset, la distribución de géneros, años, valoraciones y popularidad.

**04 - Integración con Trakt**

Conecta con la API de Trakt para obtener ratings y películas vistas del usuario. Requiere `.env` configurado.

**05 - Preprocesado semántico**

Prepara tags y señales semánticas que ayudan a explicar mejor las recomendaciones.

**06 - Recomendador híbrido final**

Calcula recomendaciones finales, aplica reglas de diversidad y genera los datasets para Power BI.

## 5. Ejecución offline directa

Este modo es el recomendado si el evaluador desea revisar el proyecto sin depender de Internet ni de una cuenta de Trakt.

Para que funcione, la carpeta entregada debe incluir:

```text
data/raw/
data/processed/
powerbi/datasets/
notebooks/
powerbi/
reports/
```

Pasos:

1. Descomprimir el proyecto.
2. Abrir la carpeta raíz.
3. Crear entorno virtual e instalar dependencias.
4. Abrir Jupyter.
5. Revisar los notebooks `01`, `02`, `03`, `05` y `06`.
6. No ejecutar de nuevo las celdas de autenticación de Trakt.
7. Abrir `powerbi/datasets/` para comprobar los resultados exportados.
8. Abrir el dashboard de Power BI.

En modo offline, el notebook `04` se puede revisar como documentación técnica de la integración con Trakt, pero no es necesario repetir la autenticación si los datos ya han sido exportados previamente.

## 6. Configuración de Trakt

Crear un archivo `.env` en la raíz del proyecto copiando `.env.example`:

```bash
copy .env.example .env
```

En macOS/Linux:

```bash
cp .env.example .env
```

Editar `.env`:

```env
TRAKT_CLIENT_ID=tu_client_id
TRAKT_CLIENT_SECRET=tu_client_secret
TRAKT_SCOPE=public
```

Después ejecutar:

```text
notebooks/04_trakt_api_integracion.ipynb
```

Durante la ejecución, el notebook solicitará autorización de la cuenta de Trakt mediante el flujo configurado en el proyecto.

## 7. Resultados esperados

El notebook final debe generar datasets en:

```text
powerbi/datasets/
```

Ficheros esperados:

```text
recomendaciones_finales.csv
perfil_usuario_trakt.csv
metricas_recomendador.csv
distribucion_recomendaciones.csv
```

Estos CSV son la base del dashboard de Power BI.

## 8. Problemas frecuentes

### Error: no se encuentran los CSV de MovieLens

Comprobar que los archivos están en:

```text
data/raw/
```

y que se llaman exactamente:

```text
movies.csv
ratings.csv
tags.csv
links.csv
```

### Error con Trakt

Revisar:

- que existe el archivo `.env`;
- que `TRAKT_CLIENT_ID` y `TRAKT_CLIENT_SECRET` están rellenados;
- que no hay espacios extra;
- que la cuenta de Trakt ha autorizado la aplicación.

### Error al abrir Power BI

Comprobar:

- que existen los cuatro CSV en `powerbi/datasets/`;
- que las rutas de origen de datos en Power BI apuntan a la carpeta correcta;
- que se ha actualizado el modelo después de mover el proyecto de carpeta.

### Error por dependencias

Actualizar pip e instalar otra vez:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```