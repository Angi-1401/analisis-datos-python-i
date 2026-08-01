# Un sensor de temperatura registró la temperatura de un lugar durante 24 horas. Recorre la lista y clasifica las temperaturas en:
# - Normal: entre 15 y 35 grados.
# - Sospechosa: menor que 15 grados o mayor que 35 grados.

# Al finalizar, muestra:
# - Número de temperaturas normales.
# - Número de temperaturas sospechosas.
# - Lista de temperaturas sospechosas.


temperaturas = [22, 24, 25, 90, 23, 24, -15, 22, 23, 120]

temp_normales = 0
temp_sospechosas = 0
lista_temp_sosp = []

for temp in temperaturas:
    if temp >= 15 and temp <= 35:
        temp_normales += 1
    else:
        temp_sospechosas += 1
        lista_temp_sosp.append(temp)

print(f"Número de temperaturas normales: {temp_normales}")
print(f"Número de temperaturas sospechosas: {temp_sospechosas}")
print(f"Lista de temperaturas sospechosas: {lista_temp_sosp}")

# Notas aclaratorias:
#
# Recuerda que si necesitas validar múltiples condiciones al mismo tiempo,
# debes utilizar los operadores lógicos 'and' y 'or'.
# - and: Devuelve True si ambas condiciones son verdaderas.
# - or: Devuelve True si al menos una de las condiciones es verdadera.
