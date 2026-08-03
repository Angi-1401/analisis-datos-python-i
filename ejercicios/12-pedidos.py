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


def procesar_pedidos(pedidos):
    pedidos_pagados = []
    total_facturado = 0
    clientes_unicos = set()

    for cliente, total, estado in pedidos:
        if total < 0:
            continue
        if estado.lower() == "pagado":
            pedidos_pagados.append((cliente, total, estado))
            total_facturado += total
            clientes_unicos.add(cliente)

    return pedidos_pagados, total_facturado, clientes_unicos


pedidos_pagados, total_facturado, clientes_unicos = procesar_pedidos(pedidos)
print(f"Cantidad de pedidos pagados válidos: {len(pedidos_pagados)}")
print(f"Total facturado: {total_facturado}")
print("Clientes que pagaron:")
for cliente in sorted(clientes_unicos):
    print(f"  {cliente}")

# Notas aclaratorias:
#
# continue se utiliza para saltar a la siguiente iteración del bucle
# si el total es negativo, evitando así procesar pedidos inválidos.
