import pandas as pd # <- Importar la biblioteca Pandas para el manejo de datos

# Cargar el archivo CSV en un DataFrame de Pandas
datos = pd.read_csv("nomina.csv")

"""Manejo de datos con Pandas:

Funciones útiles para explorar y analizar un DataFrame en Pandas.
"""

# Mostrar las primeras filas del DataFrame
print(datos.head())

# Mostrar las últimas filas del DataFrame
print(datos.tail())

# Mostrar el shape (forma) del DataFrame
print(datos.shape)

# Mostrar nombres de las columnas del DataFrame
print(datos.columns)

# Mostrar información general del DataFrame
print(datos.info())

# Mostrar estadísticas descriptivas del DataFrame
print(datos.describe())

"""Selección de columnas y filas en un DataFrame
"""

# Seleccionar una columna
print(datos["Departamento"])

# Seleccionar varias columnas
print(datos[["Nombre", "SalarioBase"]])

# Seleccionar una fila por índice
print(datos.iloc[0])  # Primera fila

# Seleccionar varias filas por índice
print(datos.iloc[0:3])  # Primeras tres filas

# Seleccionar celdas
print(datos.iloc[1, 2])  # Celda en la segunda fila y tercera columna

"""Filtrado de datos en un DataFrame
"""

# Filtrar filas según una condición
print(datos[datos["HorasExtra"] >= 5])

# ¿Cuántos trabajadores con un sueldo >= 1500 trabajaron menos de 6 horas extra?
print(datos[(datos["SalarioNeto"] >= 1500) & (datos["HorasExtra"] < 6)])

# Nota imporante:
# En Pandas, los operadores lógicos se representan con símbolos especiales:
# & -> AND
# | -> OR
# ~ -> NOT

# Ejercicios:
# Responder las siguientes preguntas utilizando Pandas:
# 1. ¿Cuántos trabajadores tienen un salario neto mayor a 2000?
# 2. ¿Cuántos trabajadores tienen un salario neto menor a 1000
# 3. ¿Cuántos trabajadores con un salario netro entre 1500 y 2500 pertenecen
#    al departamento de "TI"?
# 4. ¿Cuántos trabajadores del departamento de "Finanzas" trabajaron más de 10 horas extra?
# 5. ¿Cuántos trabajadores del departamento de "RRHH" tienen un salario neto menor a 1200 y
#    trabajaron menos de 5 horas extra?