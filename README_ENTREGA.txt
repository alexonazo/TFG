README_ENTREGA - TFG Alex Bustillo Echevarría

Proyecto:
Sistema híbrido y explicable de recomendación de películas basado en MovieLens y preferencias reales de usuario.

Estructura:

TFG_Alex_Bustillo_Echevarria/
|
|-- memoria/
|   |-- Memoria_TFG_Alex_Bustillo.docx
|   |-- Memoria_TFG_Alex_Bustillo.pdf
|
|-- presentacion/
|   |-- Presentacion_TFG_Alex_Bustillo.pptx
|   |-- Presentacion_TFG_Alex_Bustillo.pdf
|
|-- video/
|   |-- Defensa_TFG_Alex_Bustillo.mp4
|
|-- codigo/
|   |-- TFG.zip
|   |-- README_ENTREGA.txt
|
|-- powerbi/
|   |-- recomendador_peliculas_dashboard.pbix
|   |-- datasets/

Modo de revisión rápida:
1. Descomprimir TFG.zip.
2. Abrir README.md.
3. Revisar los notebooks en orden 01-06.
4. Abrir notebooks/06_recomendador_hibrido_final.ipynb para ver el resultado final.
5. Abrir powerbi/recomendador_peliculas_dashboard.pbix.
6. Revisar los CSV en powerbi/datasets/.

Modo offline:
La entrega incluye los datos procesados y los CSV finales para no depender de Trakt ni de llamadas a API durante la revisión.

Credenciales:
No se incluyen credenciales reales ni tokens personales.
No se incluye .env.
No se incluye trakt_token.json.

Uso con Trakt propio:
1. Copiar .env.example como .env.
2. Rellenar TRAKT_CLIENT_ID y TRAKT_CLIENT_SECRET.
3. Ejecutar notebooks/04_trakt_api_integracion.ipynb.
4. Continuar con notebooks/05_preprocesado_tags_semanticos.ipynb.
5. Ejecutar notebooks/06_recomendador_hibrido_final.ipynb.

Ficheros finales de Power BI:
- powerbi/datasets/recomendaciones_finales.csv
- powerbi/datasets/perfil_usuario_trakt.csv
- powerbi/datasets/metricas_recomendador.csv
- powerbi/datasets/distribucion_recomendaciones.csv
