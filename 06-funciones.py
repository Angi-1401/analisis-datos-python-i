"""
Funciones

Se trata de bloques de código reutilizables que realizan una tarea específica. En Python, las funciones se definen utilizando la palabra clave `def`, seguida del nombre de la función y paréntesis que pueden contener parámetros.
"""

def calcular_promedio(lista):
    sumatoria = 0
    for numero in lista:
        sumatoria += numero

    promedio = sumatoria / len(lista)
    print(f"Promedio de la lista: {promedio}")


lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]
lista_3 = [11, 12, 13, 14, 15]
lista_4 = [16, 17, 18, 19, 20]
lista_5 = [21, 22, 23, 24, 25]
lista_6 = [26, 27, 28, 29, 30]
lista_7 = [31, 32, 33, 34, 35]
lista_8 = [36, 37, 38, 39, 40]
lista_9 = [41, 42, 43, 44, 45]
lista_10 = [46, 47, 48, 49, 50]

calcular_promedio(lista_1)
calcular_promedio(lista_2)
calcular_promedio(lista_3)
calcular_promedio(lista_4)
calcular_promedio(lista_5)
calcular_promedio(lista_6)
calcular_promedio(lista_7)
calcular_promedio(lista_8)
calcular_promedio(lista_9)
calcular_promedio(lista_10)
