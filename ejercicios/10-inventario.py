# Una tienda tiene el siguiente inventario representado como una lista de diccionarios.
# Cada producto tiene: nombre, stock y precio.
#
# Crea una funcion llamada 'resumen_inventario()' que reciba la lista de productos y retorne:
# - total_productos: cantidad total de productos en la lista.
# - productos_sin_stock: lista con los nombres de productos cuyo stock sea 0.
# - valor_total_inventario: suma de (stock * precio) de todos los productos.
#
# Fuera de la funcion, muestra:
# - La cantidad total de productos.
# - La lista de productos sin stock.
# - El valor total del inventario.


inventario = [
    {"nombre": "Teclado", "stock": 15, "precio": 25.0},
    {"nombre": "Mouse", "stock": 0, "precio": 12.5},
    {"nombre": "Monitor", "stock": 8, "precio": 180.0},
    {"nombre": "USB", "stock": 0, "precio": 6.0},
    {"nombre": "Laptop", "stock": 4, "precio": 950.0},
]

def resumen_inventario(inventario):
    total_productos = len(inventario)
    productos_sin_stock = [producto["nombre"] for producto in inventario if producto["stock"] == 0]
    valor_total_inventario = sum(producto["stock"] * producto["precio"] for producto in inventario)

    return total_productos, productos_sin_stock, valor_total_inventario

total_productos, productos_sin_stock, valor_total_inventario = resumen_inventario(inventario)

print(f"Cantidad total de productos: {total_productos}")
print(f"Productos sin stock: {productos_sin_stock}")
print(f"Valor total del inventario: {valor_total_inventario}")

# Notas aclaratorias:
#
# Cuando una función retorna múltiples valores, se pueden desempaquetar en variables
# separadas al momento de la llamada.
# Estas variables deberán estar en el mismo orden que los valores retornados por la función
# y separadas por comas.