# Clasifica las ventas de una tienda en función de su desempeño.
# La clasificación será:
# - Bajo: ventas menores a $1000
# - Medio: ventas entre $1000 y $1999
# - Alto: ventas mayores a $2000

# Crea una función llamada 'clasificar_rendimiento()' que reciba la lista de ventas y
# retorne una nueva lista con la clasificación correspondiente a cada venta.


ventas = [850, 1250, 980, 2200, 1750, 640, 3100]


def clasificar_rendimiento(ventas):
    clasificaciones = []

    for venta in ventas:
        if venta < 1000:
            clasificaciones.append("Bajo")
        elif 1000 <= venta < 2000:
            clasificaciones.append("Medio")
        else:
            clasificaciones.append("Alto")

    return clasificaciones


rendimiento = clasificar_rendimiento(ventas)

print(f"Ventas: {ventas}")
print(f"Clasificación de rendimiento: {rendimiento}")

# Notas aclaratorias:
#
# La expresión:
#   1000 <= venta < 2000
# es equivalente a:
#   venta >= 1000 and venta < 2000
#
# Se trata de una forma más concisa y legible de escribir la condición.
