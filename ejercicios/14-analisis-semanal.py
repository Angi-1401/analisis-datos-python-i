# Una cafeteria registro sus ventas diarias de la semana.
# Cada elemento de la lista tiene el formato:
# {"dia": str, "ventas": list[int]}
# donde "ventas" representa las ventas de cada turno del dia.
#
# Crea una funcion llamada 'analisis_semanal()' que reciba la estructura y retorne:
# - total_semana: suma de todas las ventas.
# - promedio_diario: promedio de ventas por dia.
# - mejor_dia: nombre del dia con mayor venta total.
# - dias_bajos: lista de dias cuya venta total sea menor a 300.
#
# Fuera de la funcion, imprime un resumen claro de resultados.
#
# Nota:
# Puedes crear una funcion auxiliar para calcular el total por dia.


semana = [
    {"dia": "Lunes", "ventas": [120, 95, 110]},
    {"dia": "Martes", "ventas": [80, 75, 90]},
    {"dia": "Miercoles", "ventas": [150, 140, 130]},
    {"dia": "Jueves", "ventas": [60, 85, 70]},
    {"dia": "Viernes", "ventas": [200, 220, 210]},
    {"dia": "Sabado", "ventas": [180, 190, 205]},
    {"dia": "Domingo", "ventas": [90, 100, 95]},
]

def analisis_semanal(semana):
    total_semana = 0
    mejor_dia = ""
    max_ventas = 0
    dias_bajos = []

    for dia_info in semana:
        dia = dia_info["dia"]
        ventas = dia_info["ventas"]
        total_dia = sum(ventas)
        total_semana += total_dia

        if total_dia > max_ventas:
            max_ventas = total_dia
            mejor_dia = dia

        if total_dia < 300:
            dias_bajos.append(dia)

    promedio_diario = total_semana / len(semana)

    return total_semana, promedio_diario, mejor_dia, dias_bajos

total_semana, promedio_diario, mejor_dia, dias_bajos = analisis_semanal(semana)
print(f"Total de ventas de la semana: {total_semana}")
print(f"Promedio diario de ventas: {promedio_diario:.2f}")
print(f"Mejor día de ventas: {mejor_dia}")
print("Días con ventas bajas:")
for dia in dias_bajos:
    print(f"  {dia}")
