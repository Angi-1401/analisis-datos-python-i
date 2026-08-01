# Dada la siguiente lista de edades, determina cuántos registros son
# válidos (edad mayor o igual a 0) y cuantos son inválidos (edad menor a 0).


edades = [25, 34, -1, 42, 19, -5, 30, 50]

validos = 0
invalidos = 0

for edad in edades:
    if edad >= 0:
        validos += 1
    else:
        invalidos += 1

print(f"{validos} registros son válidos y {invalidos} registros son invalidos.")

# Notas aclaratorias:
#
# Las estructuras de datos sólo pueden recorrerse mediante ciclos.
# Cuando recorremos una lista con un ciclo, cada elemento de la lista se almacena en una variable temporal
# denominada iterador. En este caso, la variable iterador es 'edad'.
# Esto implica que si queremos acceder a los elementos de la lista, debemos usar el nombre del iterador.
