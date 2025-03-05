Justificación para la Validación de Datos Extraídos y Visualizaciones
Este documento explica los métodos de validación utilizados para garantizar la precisión y fiabilidad de los datos extraídos y las visualizaciones en el repositorio.

1. Validación de la Generación de Nube de Palabras
Proceso:
Se extrajeron los resúmenes de múltiples archivos XML.
Se verificó el texto extraído inspeccionando manualmente el contenido en comparación con los archivos XML originales.
Se comprobó la existencia de resúmenes vacíos o faltantes y se aseguró su correcto manejo.
Se generó la nube de palabras y se revisaron los términos comunes para comprobar su precisión.
Pasos de validación:
Se comparó el texto extraído con el contenido original del XML.
Se verificó que las palabras en la nube coincidieran con los términos más utilizados en los resúmenes.
Se ejecutó el script varias veces con diferentes conjuntos de datos para confirmar su consistencia.
2. Validación del Conteo de Figuras por Artículo
Proceso:
Se extrajeron las ocurrencias de la etiqueta <figure> en los archivos XML.
Se contó el número de figuras en cada artículo.
Se creó un gráfico de barras para la visualización.
Pasos de validación:
Se verificó manualmente el número de elementos <figure> en un subconjunto de archivos XML.
Se comparó la salida del script con los conteos manuales.
Se aseguró que los artículos sin figuras fueran representados correctamente con un valor de cero.
Se realizaron pruebas con diferentes conjuntos de datos XML para confirmar la robustez del método.
3. Validación de Enlaces Extraídos
Proceso:
Se extrajeron todos los enlaces dentro de <ref target="URL"> de los archivos XML.
Se almacenaron los resultados en un diccionario, con los nombres de los archivos como claves.
Se imprimieron y, opcionalmente, se guardaron los enlaces extraídos.
Pasos de validación:
Se verificaron manualmente los enlaces extraídos comparándolos con el contenido XML.
Se aseguró que solo se recopilaran atributos target válidos.
Se comprobaron casos especiales como URLs faltantes o malformadas.
Se probó el script con múltiples archivos XML para verificar la consistencia.