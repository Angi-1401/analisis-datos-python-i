# Un sistema registro eventos con los niveles: "INFO", "WARN" y "ERROR".
# Queremos limpiar y resumir el log.
#
# Crea una funcion llamada 'resumir_logs()' que reciba la lista de eventos.
# Cada evento tiene el formato: (nivel, mensaje)
#
# La funcion debe:
# - Normalizar el nivel a mayusculas.
# - Filtrar eventos con nivel invalido.
# - Contar cuantos eventos hay por cada nivel valido.
# - Generar una lista solo con los mensajes de ERROR.
#
# Debe retornar:
# - conteo_niveles (diccionario)
# - errores (lista)
# - invalidos (cantidad)
#
# Extra:
# Usa una comprension de listas para crear la lista de mensajes de ERROR.


eventos = [
    ("info", "Inicio de proceso"),
    ("WARN", "Uso de memoria alto"),
    ("error", "Fallo al conectar base de datos"),
    ("DEBUG", "Valor intermedio x=42"),
    ("ERROR", "Tiempo de espera agotado"),
    ("Info", "Proceso finalizado"),
]
