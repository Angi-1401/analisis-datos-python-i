# Una empresa realizo una encuesta de satisfaccion y guardo las respuestas en una lista.
# Los valores validos van del 1 al 5.
#
# Crea una funcion llamada 'analizar_encuesta()' que reciba la lista de respuestas.
# La funcion debe:
# - Ignorar los valores invalidos (menores a 1 o mayores a 5).
# - Calcular el promedio de respuestas validas.
# - Contar cuantas respuestas hay por cada valor (1, 2, 3, 4 y 5).
#
# La funcion debe retornar:
# - promedio
# - conteos (diccionario con clave 1..5 y su cantidad)
# - invalidas (cantidad de respuestas invalidas)
#
# Fuera de la funcion, imprime los resultados con mensajes claros.


respuestas = [5, 4, 3, 2, 5, 1, 0, 6, 4, 3, 2, -1, 5, 4]
