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

def analizar_encuesta(respuestas):
    conteos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    total_validas = 0
    suma_validas = 0
    invalidas = 0

    for respuesta in respuestas:
        if 1 <= respuesta <= 5:
            conteos[respuesta] += 1
            suma_validas += respuesta
            total_validas += 1
        else:
            invalidas += 1

    promedio = suma_validas / total_validas if total_validas > 0 else 0

    return promedio, conteos, invalidas

promedio, conteos, invalidas = analizar_encuesta(respuestas)
print(f"Promedio de respuestas válidas: {promedio}")
print("Conteo de respuestas válidas:")
for valor, cantidad in conteos.items():
    print(f"  {valor}: {cantidad}")
print(f"Respuestas inválidas: {invalidas}")

# Notas aclaratorias:
#
# La expresión:
#   conteos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
# crea un diccionario con claves del 1 al 5 y valores iniciales de 0.
#
# Por otro lado, la expresión:
#   promedio = suma_validas / total_validas if total_validas > 0 else 0
# calcula el promedio de respuestas válidas, evitando la división por
# cero en caso de que no haya respuestas válidas.