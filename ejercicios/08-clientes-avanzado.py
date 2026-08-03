# Limpia la lista dada a continuación.

# Crea una función llamada 'normalizar_clientes()' que reciba la lista de clientes.
# La función debe eliminar los espacios en blanco al inicio y al final de cada nombre y convertirlos al formato de título.

# Nota:
# Utiliza la función 'strip()' para eliminar los espacios en blanco y
# la función 'title()' para convertir el nombre al formato de título.


clientes = [" ana ", "CARLOS", "mAría", " PEDRO ", "luisa"]


def normalizar_clientes(clientes):
    clientes_normalizados = []

    for cliente in clientes:
        cliente_normalizado = cliente.strip().title()
        clientes_normalizados.append(cliente_normalizado)
    
    return clientes_normalizados


clientes_normalizados = normalizar_clientes(clientes)

print(f"Lista original de clientes: {clientes}")
print(f"Lista normalizada de clientes: {clientes_normalizados}")
