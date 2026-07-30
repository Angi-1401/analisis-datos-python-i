"""Condicionales"""

"""1.1.
Simula un cajero automático.
El algoritmo debe pedir:
- Saldo disponible en la cuenta.
- Cantidad a retirar.

Reglas:
- Si la cantidad a retirar es mayor que el saldo disponible, mostrar un mensaje de error.
- Si el retirno no es múltiplo de 10, mostrar un mensaje de error.
- Si todo es corecto, mostrar el nuevo saldo disponible después del retiro.
"""

"""1.2.
Crea un algoritmo que calcule el precio final de una compra.
El usuario ingresa:
- Precio total de la compra.
- Si tiene tarjeta de cliente (si/no).
- Día de la semana.

Reglas:
- Si compra más de $100, obtiene un 10% de descuento.
- Si tiene tarjeta de cliente, obtiene un 5% de descuento adicional.
- Si es lunes, obtiene un 5% de descuento adicional.
- Los descuentos se acumulan, es decir, se aplican uno tras otro sobre el precio final.
"""


"""Ciclos
"""

"""2.1.
Dada la siguiente lista de edades, determina cuántos registros son válidos (edad mayor o igual a 0) y cuantos son inválidos (edad menor a 0).
"""

edades = [25, 34, -1, 42, 19, -5, 30, 50]

"""2.2.
Una tienda registró las ventas de los últimos siete días. Recorre la lista y calcula:
- Ventas totales.
- Promedio de ventas.
- Cantidad de ventas mayores a $1500
"""

ventas = [1200, 980, 1500, 760, 2100, 1850, 950]

"""2.3.
Un sensor de temperatura registró la temperatura de un lugar durante 24 horas. Recorre la lista y clasifica las temperaturas en:
- Normal: entre 15 y 35 grados.
- Sospechosa: menor que 15 grados o mayor que 35 grados.

Al finalizar, muestra:
- Número de temperaturas normales.
- Número de temperaturas sospechosas.
- Lista de temperaturas sospechosas.
"""

temperaturas = [22, 24, 25, 90, 23, 24, -15, 22, 23, 120]

"""2.4.
Dada una lista de clientes, recorre la lista y crea una nueva lista que sólo contenga nombres válidos.
Considera inválidos:
- None
- Cadenas vacías ("")
- Espacios en blanco (" ")

Al finalizar, muestra:
- Cantidad de registros originales.
- Cantidad de registros válidos.
- Cantidad de registros eliminados.
- La nueva lista de clientes válidos.
"""

clientes = ["Ana", "", "Carlos", " ", "María", None, "Pedro", ""]


"""Funciones y List Comprehension
"""

"""3.1.
La lista presentada a continuación contiene las ventas registradas de un día, sin embargo, algunos valores son incorrectos porque corresponde a devoluciones o errores de captura.

Crea un función llamada 'obtener_ventas_validas()' que reciba la lista de ventas.
Dentro de la función, crea una nueva lista que contenga sólo los valores válidos (mayores o iguales a 0) y retorna la nueva lista.
La función debe devolver la nueva lista.

Fuera de la función, muestra:
- La lista original de ventas.
- La lista de ventas válidas.
- La cantidad de registros eliminados.
"""

ventas = [1200, -150, 980, 2100, -50, 1850, 760, -300]

"""3.2.
Limpia la lista dada a continuación.

Crea una función llamada 'normalizar_clientes()' que reciba la lista de clientes.
La función debe eliminar los espacios en blanco al inicio y al final de cada nombre y convertirlos al formato de título.

Nota:
Utiliza la función 'strip()' para eliminar los espacios en blanco y la función 'title()' para convertir el nombre al formato de título.
"""

clientes = [" ana ", "CARLOS", "mAría", " PEDRO ", "luisa"]

"""3.3.
Clasifica las ventas de una tienda en función de su desempeño.
La clasificación será:
- Bajo: ventas menores a $1000
- Medio: ventas entre $1000 y $1999
- Alto: ventas mayores a $2000

Crea una función llamada 'clasificar_rendimiento()' que reciba la lista de ventas y retorne una nueva lista con la clasificación correspondiente a cada venta.
"""

ventas = [850, 1250, 980, 2200, 1750, 640, 3100]
