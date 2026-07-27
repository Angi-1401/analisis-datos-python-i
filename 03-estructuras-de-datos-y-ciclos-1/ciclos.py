"""Python

Ciclos

Permiten ejecutar un bloque de código varias veces, mientras se cumpla una condición.
"""

"""
Ciclo for (para)

Permite iterar sobre un rango o secuencia finita (lista, tupla, diccionario, conjunto o cadena de caracteres) y ejecutar un bloque de código para cada elemento de la secuencia.
"""

for i in range(1,11):
    print(f"7 x {i} = {7 * i}")


notas = [20, 18, 15, 14, 12, 10, 9]
suma = 0

for nota in notas:
    suma += nota # suma = suma + nota
    print(f"Nota: {nota}, Suma acumulada: {suma}")

promedio = suma / len(notas)
print(f"Promedio: {promedio}")