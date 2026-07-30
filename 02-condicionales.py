"""Python

Condicionales

Las condicionales permiten ejecutar código de forma condicional.
Esto es, ejecutar código si y sólo si una serie de condiciones establecidas se cumple.

Por ejemplo:
Si mi presupuesto es mayor al costo de la hamburguesa, entonces puedo comprarla.
Si mi presupuesto es mayor al costo del perrito caliente, entonces puedo comprarlo.
Si no, debo prepara comida en casa.
"""

costo_hamburgesa = 3.5
costo_perrito_caliente = 2

presupuesto = 2.7

# El bloque de código identado sólo se ejecuta si la condición es verdadera.
if presupuesto >= costo_hamburgesa:
    print("Puedo comprar una hamburguesa.")


# El primer bloque de código se ejecuta si la condicón es verdadera;
# sino, se ejecuta el segundo.
if presupuesto >= costo_hamburgesa:
    print("Puedo comprar una hamburguesa.")
else:
    print("Debo preparar comida en casa.")

# Primero se evalúa prespuesto >= costo_hamburguesa
#   Si el resultado es verdadero, se ejecuta su bloque de código.
#   Si el resultado es falso, se evalúa presupuesto >= costo_perrito_caliente.
# La segunda condición evaluada sigue el mismo proceso.
# Si esta último también resulta falsa, el código ejecutará el bloque else.
if presupuesto >= costo_hamburgesa:
    print("Puedo comprar una hamburguesa.")
elif presupuesto >= costo_perrito_caliente:
    print("Puedo comprar un perrito caliente.")
else:
    print("Debo preparar comida en casa.")

# Esta línea no pertenece a ninguno de los bloques de las condicionales,
# por lo que su ejecutará siempre.
print("Todo estuvo delicioso.")


"""
Estructura de una condicional:

if condicion_a_evaluar:
    # Código a ejecutar si la condición resulta en True.
elif condicion_a_evaluar_2:
    # Código a ejecutar si la condición resulta en True.
.
.
.
elif condicion_a_evaluar_n:
    # Código a ejecutar si la condición resulta en True.
else:
    # Código a ejecutar si la condición resulta en False.

Nota:
Tanto elif como else no son obligatorios.
    - elif se usará si se necesitan evaluar múltiples condiciones que resulten
      en respuestas (bloque de código) distintos
    - else se usará si es necesario ejecutar una acción cuando la condición es false.
"""

# Ejercicios

# Escribir un programa que permita determinar si un número es par o impar.
# Si n es divisible entre 2 (n % 2 == 0), entonces es par. Sino, es impar.

n = 1567
if n % 2 == 0:
    print(f"{n} es par.")
else:
    print(f"{n} es impar.")

# Escribir un programa que permita graduar una nota de acuerdo a la siguiente tabla de
# valores:
#   A: Nota entre 20 y 18 pts.
#   B: Nota entre 17 y 15 pts.
#   C: Nota entre 14 y 12 pts.
#   D: Nota entre 11 y 10 pts.
#   Reprobado: Nota menor o igual a 9 pts.

nota = 13

if nota <= 18 and nota >= 20:
    print(" La Calificación es: A")
elif nota >= 15 and nota <= 17:
    print("La Calificación es : B")
elif nota >= 12 and nota <= 14:
    print("La Calificación es: C")
elif nota >= 10 and nota <= 11:
    print("La Calificación es: D")
else:
    print("Reprobado")
