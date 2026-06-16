# Dashboard Power BI automatico

Este directorio contiene una base editable para Power BI Desktop generada desde los CSV finales del TFG.

## Que se ha generado

- `recomendador_peliculas_dashboard.pbip`: acceso principal al proyecto Power BI.
- `recomendador_peliculas_dashboard.Report/`: definicion PBIR del reporte con cinco paginas base.
- `recomendador_peliculas_dashboard.SemanticModel/`: modelo semantico con las cuatro tablas CSV.
- `build_powerbi_assets.py`: validacion de datos y generacion de previews PNG.
- `../reports/figures/powerbi_preview/`: imagenes preliminares para revisar o incluir en memoria.

## CSV usados

El dashboard usa estos archivos, sin modificarlos:

- `powerbi/datasets/recomendaciones_finales.csv`
- `powerbi/datasets/perfil_usuario_trakt.csv`
- `powerbi/datasets/metricas_recomendador.csv`
- `powerbi/datasets/distribucion_recomendaciones.csv`

## Como abrirlo en Power BI Desktop

1. Abre Power BI Desktop.
2. Activa las opciones preview si tu version lo pide:
   - `Archivo > Opciones y configuracion > Opciones > Caracteristicas en vista previa`.
   - Activa `Power BI Project (.pbip)` y, si aparece, `Store reports using enhanced metadata format (PBIR)`.
3. Ve a `Archivo > Abrir`.
4. Abre `powerbi/recomendador_peliculas_dashboard.pbip`.
5. Si Power BI pregunta por origen de datos, revisa que apunte a `C:\Users\alexo\Desktop\TFG\powerbi\datasets\`.
6. Pulsa `Actualizar`.
7. Edita el diseno y guarda.
8. Para entrega final, usa `Archivo > Guardar como` y guarda `powerbi/recomendador_peliculas_dashboard.pbix`.

## Si Power BI no abre el proyecto

PBIP/PBIR sigue en preview y puede cambiar entre versiones de Power BI Desktop. Si Desktop no abre el proyecto:

1. Abre Power BI Desktop y crea un reporte nuevo.
2. Importa manualmente los cuatro CSV desde `powerbi/datasets/`.
3. Usa `POWERBI_DASHBOARD_GUIDE.md` como plano de paginas y visuales.
4. Usa los PNG de `reports/figures/powerbi_preview/` como referencia visual.
5. Guarda el resultado como `powerbi/recomendador_peliculas_dashboard.pbix`.

## Como refrescar datos

1. Regenera o actualiza los CSV desde el flujo del proyecto.
2. Ejecuta:

```powershell
.\.venv\Scripts\python.exe powerbi\build_powerbi_assets.py
```

3. Abre el `.pbip` o `.pbix` en Power BI Desktop.
4. Pulsa `Actualizar`.

## Paginas incluidas

- `Resumen`: tarjetas de metricas principales y texto descriptivo del sistema.
- `Perfil Trakt`: distribucion del historial, generos, decadas y tabla de perfil.
- `Top recomendaciones`: tabla principal y barras del score final.
- `Explicabilidad`: riesgo frente a margen, senal dominante y tabla explicativa.
- `Diversidad`: distribuciones por genero, decada, tipo de recomendacion y rama.

## Visuales a revisar o editar

Revisa especialmente:

- Formato de tarjetas de `Resumen`.
- Orden de la barra de `Top recomendaciones`, idealmente por `rank` ascendente o `final_recommendation_score` descendente.
- Legibilidad de `explanation_display` en tablas.
- Filtros de `Diversidad`, usando `dimension` para separar cada grafico.
- Titulos y ajuste de ancho de columnas.

## Notas de seguridad

No se generan credenciales, no se usa Power BI Service y no se publica nada online. El modelo no crea relaciones para evitar filtrados incorrectos entre perfil y recomendaciones.
