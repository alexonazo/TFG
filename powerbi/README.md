# Power BI

La carpeta `powerbi/` contiene los elementos necesarios para visualizar los resultados del recomendador de películas.

## 1. Datasets utilizados

El notebook final genera cuatro CSV en:

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

## 2. Significado de los datasets

### `recomendaciones_finales.csv`

Contiene la lista final de películas recomendadas, sus puntuaciones y las columnas explicativas necesarias para justificar la recomendación.

### `perfil_usuario_trakt.csv`

Resume el perfil construido a partir de ratings y películas vistas de Trakt.

### `metricas_recomendador.csv`

Contiene métricas generales del sistema: puntuaciones, diversidad, señales utilizadas y valores agregados para evaluar el comportamiento del recomendador.

### `distribucion_recomendaciones.csv`

Permite analizar la distribución final de las recomendaciones por categorías, géneros o ramas de explicación.

## 3. Abrir el dashboard

1. Abrir Power BI Desktop.
2. Abrir el proyecto `recomendador_peliculas_dashboard.pbip` o el `.pbix` incluido en la entrega.
3. Comprobar que los orígenes de datos apuntan a:

```text
powerbi/datasets/
```

4. Pulsar **Actualizar**.
5. Revisar las visualizaciones.

## 4. Problemas frecuentes

### Power BI no encuentra los CSV

Solución:

1. Abrir **Transformar datos**.
2. Entrar en configuración de origen.
3. Cambiar la ruta a la carpeta local donde esté `powerbi/datasets/`.
4. Aplicar cambios y actualizar.

### Los datos no se actualizan

Solución:

1. Comprobar que los CSV no están abiertos en Excel.
2. Cerrar Excel.
3. Actualizar de nuevo en Power BI.

### El dashboard muestra valores antiguos

Solución:

1. Ejecutar `notebooks/06_recomendador_hibrido_final.ipynb`.
2. Confirmar que los CSV se han sobrescrito.
3. Actualizar Power BI.
