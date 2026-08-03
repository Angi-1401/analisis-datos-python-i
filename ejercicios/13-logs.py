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


def resumir_logs(eventos):
    conteo_niveles = {"INFO": 0, "WARN": 0, "ERROR": 0}
    errores = []
    invalidos = 0

    for nivel, mensaje in eventos:
        nivel_normalizado = nivel.upper()
        if nivel_normalizado in conteo_niveles:
            conteo_niveles[nivel_normalizado] += 1
            if nivel_normalizado == "ERROR":
                errores.append(mensaje)
        else:
            invalidos += 1

    return conteo_niveles, errores, invalidos


conteo_niveles, errores, invalidos = resumir_logs(eventos)
print("Conteo de niveles:")
for nivel, cantidad in conteo_niveles.items():
    print(f"  {nivel}: {cantidad}")
print(f"Cantidad de eventos inválidos: {invalidos}")
print("Mensajes de ERROR:")
for mensaje in errores:
    print(f"  {mensaje}")
