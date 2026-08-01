# Una tienda online registra pedidos con el formato:
# (cliente, total, estado)
#
# Crea una funcion llamada 'procesar_pedidos()' que reciba la lista de pedidos y retorne:
# - pedidos_pagados: lista de pedidos cuyo estado sea "pagado".
# - total_facturado: suma de los totales de los pedidos pagados.
# - clientes_unicos: conjunto (set) con los nombres de clientes que pagaron.
#
# Reglas:
# - Ignora pedidos con total negativo.
# - Considera el estado sin importar mayusculas/minusculas.
#
# Fuera de la funcion, muestra:
# - Cantidad de pedidos pagados validos.
# - Total facturado.
# - Lista ordenada alfabeticamente de clientes que pagaron.


pedidos = [
    ("Ana", 120.5, "pagado"),
    ("Luis", 80.0, "PAGADO"),
    ("Marta", -15.0, "pagado"),
    ("Jose", 45.0, "pendiente"),
    ("Ana", 210.0, "Pagado"),
    ("Carla", 60.0, "cancelado"),
    ("Luis", 35.5, "pagado"),
]
