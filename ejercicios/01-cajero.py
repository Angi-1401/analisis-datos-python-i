# Simula un cajero automático.
# El algoritmo debe pedir:
# - Saldo disponible en la cuenta.
# - Cantidad a retirar.

# Reglas:
# - Si la cantidad a retirar es mayor que el saldo disponible, mostrar un mensaje de error.
# - Si el retirno no es múltiplo de 10, mostrar un mensaje de error.
# - Si todo es corecto, mostrar el nuevo saldo disponible después del retiro.


saldo_disponible = float(input("Ingrese el saldo disponible en la cuenta: "))
cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))

if cantidad_retiro > saldo_disponible:
 print("Error: La cantidad a retirar es mayor que el saldo disponible.")
elif cantidad_retiro % 10 != 0:
    print("Error: La cantidad a retirar no es múltiplo de 10.")
else:
    nuevo_saldo = saldo_disponible - cantidad_retiro
    print(f"Nuevo saldo disponible: {nuevo_saldo}")

# Notas aclaratorias:
#
# - input(): Permite al usuario ingresar datos por teclado a través de la consola.
# - float(): Convierte un valor a tipo flotante (decimal).
#
# ¿Por qué utilizamos float() en los inputs()?
# Porque input() devuelve un valor de tipo cadena (str), y necesitamos
# convertirlo a un número decimal para poder realizar operaciones
# matemáticas con él.
#
# Además de float(), también existen:
# - int(): Convierte un valor a tipo entero.
# - str(): Convierte un valor a tipo cadena de texto.