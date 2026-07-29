# Crear una lista con los cuadrados de los números del 1 al 5.
# [1, 4, 9, 16, 25]

# cuadrados = [1, 4, 9, 16, 25]

cuadrados = []
for i in range(1, 6):
    cuadrados.append(i**2)

print(f"Lista de cuadrados: {cuadrados}")

cuadrados = [i**2 for i in range(1, 6)]
print(f"Lista de cuadrados (usando comprensión de listas): {cuadrados}")


# Filtrar la lista con el objetivo de obtener únicamente los números pares de la lista original.

secuencia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
for numero in secuencia:
    if numero % 2 == 0:
        pares.append(numero)

print(f"Lista de números pares: {pares}")

pares = [numero for numero in secuencia if numero % 2 == 0]
print(f"Lista de números pares (usando comprensión de listas): {pares}")


salarios = [1500, 2000, 2500, 3000, 3500]

# Incrementar cada salario en un 10%
salarios_actualizados = []
for salario in salarios:
    salarios_actualizados.append(salario * 1.1)

print(f"Salarios actualizados: {salarios_actualizados}")

salarios_actualizados = [salario * 1.1 for salario in salarios]
print(f"Salarios actualizados (usando comprensión de listas): {salarios_actualizados}")