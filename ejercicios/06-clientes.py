# Dada una lista de clientes, recorre la lista y crea una nueva lista que sólo contenga nombres válidos.
# Considera inválidos:
# - None
# - Cadenas vacías ("")
# - Espacios en blanco (" ")

# Al finalizar, muestra:
# - Cantidad de registros originales.
# - Cantidad de registros válidos.
# - Cantidad de registros eliminados.
# - La nueva lista de clientes válidos.

# Nota:
# Utiliza la función 'strip()' para eliminar los espacios en blanco


clientes = ["Ana", "", "Carlos", " ", "María", None, "Pedro", ""]

clientes_validos = []
eliminados = 0

for cliente in clientes:
    if cliente is not None and cliente.strip() != "":
        clientes_validos.append(cliente)
    else:
        eliminados += 1

print(f"Cantidad de registros originales: {len(clientes)}")
print(f"Cantidad de registros válidos: {len(clientes_validos)}")
print(f"Cantidad de registros eliminados: {eliminados}")
print(f"Lista de clientes válidos: {clientes_validos}")

# Notas aclaratorias:
#
# - strip(): Elimina los espacios en blanco al inicio y al final de una cadena.
