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

"""
Plantilla de un ciclo for

for variable in secuencia:
    bloque de código
"""

# Imprimir una pirámide de asteriscos de 5 niveles.

for i in range(1, 6):
    print("*" * i)


"""
Ciclos while (mientras)

Permite ejecutar indefinidamente un bloque de código entre tanto la condición dada para su ejeción resulte en verdadero (True). Cuando la condición resulte en falso (False), el ciclo se detendrá.
"""

suma = 0
respuesta = "si"

while respuesta == "si":
    suma += 1 # suma = suma + 1
    print(f"El valor acumulado es: {suma}")
    print("¿Desea continuar sumando? (si/no)")
    respuesta = input("Respuesta: ")
