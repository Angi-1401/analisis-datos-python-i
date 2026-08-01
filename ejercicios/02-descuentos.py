# Crea un algoritmo que calcule el precio final de una compra.
# El usuario ingresa:
# - Precio total de la compra.
# - Si tiene tarjeta de cliente (si/no).
# - Día de la semana.

# Reglas:
# - Si compra más de $100, obtiene un 10% de descuento.
# - Si tiene tarjeta de cliente, obtiene un 5% de descuento adicional.
# - Si es lunes, obtiene un 5% de descuento adicional.
# - Los descuentos se acumulan, es decir, se aplican uno tras otro sobre el precio final.


precio_total = float(input("Ingrese el precio total de la compra: "))
tiene_tarjeta = input("¿Tiene tarjeta de cliente? (si/no): ").lower()
dia_semana = input("Ingrese el día de la semana: ").lower()

descuento = 0

if precio_total > 100:
    descuento += precio_total * 0.10

if tiene_tarjeta == "si":
    descuento += precio_total * 0.05

if dia_semana == "lunes":
    descuento += precio_total * 0.05

precio_final = precio_total - descuento
print(f"Precio final de la compra: {precio_final}")

# Notas aclaratorias:
#
# - lower(): Convierte una cadena de texto a minúsculas.
# - upper(): Convierte una cadena de texto a mayúsculas.
#
# ¿Por qué nuestros ifs están separados y no anidados con elif?
# Porque queremos que se apliquen todos los descuentos posibles, no solo uno.
# Las condiciones en elif sólo se evalúan si la condición anterior no se cumple.
# Como todas nuestras condiciones son independientes, usamos if separados
# para que se puedan aplicar todas.
