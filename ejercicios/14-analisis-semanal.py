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
