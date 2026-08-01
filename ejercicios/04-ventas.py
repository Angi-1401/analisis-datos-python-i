# Una tienda registró las ventas de los últimos siete días. Recorre la lista y calcula:
# - Ventas totales.
# - Promedio de ventas.
# - Cantidad de ventas mayores a $1500


ventas = [1200, 980, 1500, 760, 2100, 1850, 950]

total_ventas = 0
ventas_grandes = 0

for venta in ventas:
    total_ventas += venta

    if venta > 1500:
        ventas_grandes += 1

print(f"Ventas totales: {total_ventas}")
print(f"Promedio de ventas: {total_ventas / len(ventas)}")
print(f"Cantidad de ventas mayores a $1500: {ventas_grandes}")

# Notas aclaratorias:
#
# La expresión:
#   total_ventas += venta
# es equivalente a:
#   total_ventas = total_ventas + venta
#
# Se trata de una forma más concisa de escribir la operación de suma y asignación en una sola línea.
# El mismo truco puede usarse con todos los operadores aritméticos, por ejemplo:
#
#   acumulador -= valor  # Resta y asigna
#   acumulador *= valor  # Multiplica y asigna
#   acumulador /= valor  # Divide y asigna
#   acumulador %= valor  # Módulo y asigna
