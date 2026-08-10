import pandas as pd


def write_csv(df, filename):
    """
    Función para guardar un DataFrame en un archivo CSV.

    Parámetros:
    df (DataFrame): El DataFrame que se desea guardar.
    filename (str): El nombre del archivo CSV de salida.
    """
    df.to_csv(filename, index=False)


datos = pd.read_csv("nomina.csv")

datos_filtrados = datos[
    (datos["SalarioNeto"] >= 1500)
    & (datos["SalarioNeto"] <= 2500)
    & (datos["Departamento"] == "TI")
]

write_csv(datos_filtrados, "nomina_filtrada.csv")

"""
También podemos decidir no usar la función write_csv y guardar el DataFrame directamente en un archivo CSV utilizando el método to_csv de Pandas:

datos_filtrados.to_csv("nomina_filtrada.csv", index=False)
"""
