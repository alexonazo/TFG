# Configuración de Trakt

Esta guía explica cómo conectar el proyecto con una cuenta de Trakt para obtener ratings y películas vistas reales del usuario.

## 1. Qué aporta Trakt al proyecto

Trakt se utiliza para enriquecer el recomendador con información personal real del usuario:

- películas valoradas;
- películas vistas;
- preferencias implícitas y explícitas;
- construcción de un perfil de usuario más realista;
- exclusión de películas ya vistas;
- explicación de recomendaciones en función de gustos reales.

El sistema también puede revisarse offline si ya se han generado previamente los datasets finales.

## 2. Crear una aplicación en Trakt

Pasos generales:

1. Entrar en Trakt con una cuenta personal.
2. Acceder a la sección de aplicaciones/API de Trakt.
3. Crear una nueva aplicación.
4. Copiar el `Client ID`.
5. Copiar el `Client Secret`.
6. Guardar ambos valores solo en el archivo `.env`.

No se deben incluir estas credenciales en notebooks, código, capturas ni repositorio.

## 3. Crear el archivo `.env`

En la raíz del proyecto existe:

```text
.env.example
```

Copiarlo como:

```text
.env
```

Contenido esperado:

```env
TRAKT_CLIENT_ID=tu_client_id
TRAKT_CLIENT_SECRET=tu_client_secret
TRAKT_SCOPE=public
```

Ejemplo de comandos.

Windows:

```bash
copy .env.example .env
```

macOS/Linux:

```bash
cp .env.example .env
```

Después abrir `.env` con un editor de texto y sustituir los valores.

## 4. Ejecutar la integración

Abrir:

```text
notebooks/04_trakt_api_integracion.ipynb
```

Ejecutar las celdas en orden. El notebook realiza el proceso de autenticación y obtiene los datos necesarios de la cuenta.

Después de este paso, continuar con:

```text
notebooks/05_preprocesado_tags_semanticos.ipynb
notebooks/06_recomendador_hibrido_final.ipynb
```

## 5. Ficheros sensibles

No deben subirse a GitHub ni incluirse en capturas:

```text
.env
data/processed/trakt_token.json
```

El archivo `.env.example` sí puede subirse porque no contiene credenciales reales.

## 6. Uso con otra cuenta de Trakt

Para usar otra cuenta:

1. Eliminar o apartar el token anterior si existe.
2. Configurar `.env` con la aplicación propia.
3. Ejecutar de nuevo `04_trakt_api_integracion.ipynb`.
4. Autorizar la cuenta cuando el notebook lo solicite.
5. Ejecutar de nuevo `05` y `06`.

Esto generará recomendaciones adaptadas al nuevo usuario.

## 7. Uso offline sin Trakt

Para revisar el proyecto sin cuenta de Trakt:

1. Usar la carpeta de entrega con `data/processed/` ya generada.
2. No ejecutar de nuevo el notebook `04`.
3. Revisar el notebook `04` como documentación del proceso.
4. Ejecutar o revisar directamente el notebook `06` si los datos intermedios ya están disponibles.
5. Abrir los CSV finales de `powerbi/datasets/`.

Este modo es útil para corrección y demostración, ya que evita depender de credenciales personales.

