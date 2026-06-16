# Guia de montaje del dashboard en Power BI

Usa esta guia si Power BI Desktop no acepta el proyecto PBIP/PBIR generado o si prefieres montar los visuales manualmente.

## Modelo

Importa los cuatro CSV de `powerbi/datasets/` como tablas:

- `recomendaciones_finales`
- `perfil_usuario_trakt`
- `metricas_recomendador`
- `distribucion_recomendaciones`

No crees relaciones salvo que las necesites explicitamente. Para este dashboard base es mas seguro dejar las tablas independientes.

## Resumen

Fuente: `metricas_recomendador`.

Visuales:

- Tarjeta `total_recommendations`.
- Tarjeta `total_candidates`.
- Tarjeta `trakt_ratings_mapped`.
- Tarjeta `trakt_watched_mapped`.
- Tarjeta `false_positive_risk_mean`.
- Cuadro de texto: `Sistema hibrido de recomendacion de peliculas basado en MovieLens, Trakt, perfil explicable, similitud de contenido, senal colaborativa y control de riesgo.`

## Perfil Trakt

Fuente: `perfil_usuario_trakt`.

Visuales:

- Barras: eje `profile_type`, valores recuento de `title`. Titulo: `Distribucion del historial Trakt mapeado`.
- Barras: eje `main_genre`, valores recuento de `title`, leyenda `profile_type`. Titulo: `Generos presentes en el perfil del usuario`.
- Barras: eje `decade`, valores recuento de `title`, leyenda `profile_type`. Titulo: `Distribucion temporal del perfil`.
- Tabla: `title`, `year`, `genres`, `user_rating_5`, `profile_type`.

## Top recomendaciones

Fuente: `recomendaciones_finales`.

Visuales:

- Tabla: `rank`, `title`, `year`, `main_genre`, `final_recommendation_score`, `recommendation_bucket_label`, `recommendation_branch`, `dominant_signal_label`, `temporal_affinity_label`, `explanation_display`.
- Barras horizontales: eje Y `title`, eje X `final_recommendation_score`. Ordena por `rank` ascendente o score descendente. Titulo: `Score final de recomendacion`.

## Explicabilidad

Fuente: `recomendaciones_finales`.

Visuales:

- Dispersion: X `false_positive_risk`, Y `preference_margin_score`, tamano `final_recommendation_score`, detalles `title`, leyenda `recommendation_bucket_label`. Titulo: `Margen positivo frente a riesgo de falso positivo`.
- Barras: eje `dominant_signal_label`, valores recuento de `title`. Titulo: `Senal principal de explicacion`.
- Tabla: `rank`, `title`, `recommendation_bucket_label`, `dominant_signal_label`, `temporal_affinity_label`, `anchor_movies_matched`, `explanation_display`.

## Diversidad

Fuente: `distribucion_recomendaciones`.

Crea cuatro barras usando filtro visual sobre `dimension`:

- `dimension = main_genre`: eje `category`, valores `count`. Titulo: `Distribucion por genero principal`.
- `dimension = decade`: eje `category`, valores `count`. Titulo: `Distribucion por decada`.
- `dimension = recommendation_bucket_label`: eje `category`, valores `count`. Titulo: `Distribucion por tipo de recomendacion`.
- `dimension = recommendation_branch`: eje `category`, valores `count`. Titulo: `Distribucion por rama de gusto`.
