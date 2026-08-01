# La lista presentada a continuación contiene las ventas registradas de un día, sin embargo, algunos valores son incorrectos porque corresponde a devoluciones o errores de captura.

# Crea un función llamada 'obtener_ventas_validas()' que reciba la lista de ventas.
# Dentro de la función, crea una nueva lista que contenga sólo los valores válidos (mayores o iguales a 0) y retorna la nueva lista.
# La función debe devolver la nueva lista.

# Fuera de la función, muestra:
# - La lista original de ventas.
# - La lista de ventas válidas.
# - La cantidad de registros eliminados.


ventas = [1200, -150, 980, 2100, -50, 1850, 760, -300]


def obtener_ventas_validas(ventas):
    ventas_validas = [venta for venta in ventas if venta >= 0]
    return ventas_validas


ventas_validas = obtener_ventas_validas(ventas)
registros_eliminados = len(ventas) - len(ventas_validas)

print(f"Lista original de ventas: {ventas}")
print(f"Lista de ventas válidas: {ventas_validas}")
print(f"Cantidad de registros eliminados: {registros_eliminados}")

# Notas aclaratorias:
#
# El objetivo de la compresión de listas es crear una nueva lista a partir de otra existente
# de forma eficiente y concisa. La sintaxis básica es:
#   nueva_lista = [expresion for item in lista if condicion]
#
# Donde:
# - expresion: es el valor que se agregará a la nueva lista.
# - item: es el elemento actual de la lista original.
# - lista: es la lista original que se está recorriendo.
# - condicion: es una expresión booleana que filtra los elementos que se incluirán en la nueva lista.
