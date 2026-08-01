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
