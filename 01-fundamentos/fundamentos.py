"""Python

Fundamentos básicos de programación
"""

# Imprimir mensajes en consola
print("¡Hola, mundo!")

"""Variables

Son espacios (o cajitas) donde se pueden guardar datos.
Todas las variables tienen un nombre y un valor.

Este valor pertenece a uno de los siguientes tipos:
    - Integer (Números enteros)
    - Float (Números flotantes o decimales)
    - String (Texto)
    - Booleanos (Admite uno de dos posibles valores: True o False)
    - None (Valores vacíos o ausencia de valores)
"""

# Declarar variables de cada tipo
entero = 12
flotante = 3.1416
texto = "Empanada"
booleano = True
vacio = None

"""Nota

Las variables cuyo nombre esté compuesto por dos o más palabras, deben ser escritas de
cualquiera de las siguientes formas:
    valor_max (Estructura recomendada)
    valorMax

No se deben usar nunca espacios, ni tampoco otros caracteres especiales.
"""

# Las variables pueden ver sus valores reemplazados en cualquier línea de código
sorpresa = 15
print("El valor de 'sorpresa' es: " + sorpresa)

sorpresa = 18
print(
    f"Ahora el valor de 'sorpresa' es: {sorpresa}"
)  # Esta es la forma estándar de imprimir variables en texto


"""Operadores aritméticos

Permite realizar operaciones matemáticas simples.
"""

a = 18
b = 9

print(a + b)  # Suma
print(a - b)  # Resta
print(a * b)  # Multiplicación
print(a / b)  # División
print(a**b)  # Potenciación
print(a % b)  # Módulo (Resto de una división)

"""Operadores relacionales

Permite comparar valores numéricos usando igualdades y desigualdades matemáticas.
El resultado siempre será una expresión booleana: True para verdadero, False para falso.
"""

print(a == b)  # Igual que
print(a != b)  # Diferente que
print(a > b)  # Mayor que
print(a < b)  # Menor que
print(a >= b)  # Mayor o igual que
print(a <= b)  # Menor o igual que

"""Operadores lógicos

Permiten comparar valores booleanos utilizando lógica.
El resultado siempre será una expresión booleana: True para verdadero, False para falso.
"""

x = True
y = False

# Operador AND
# Devuelve True sólo si todas las condiciones resultan en True.
print(x and y)

# Operador OR
# Devuelve True si al menos una de las condiciones resulta en True.
print(x or y)

# Operador NOT
# Convierte True en False y viceversa
print(not x)
