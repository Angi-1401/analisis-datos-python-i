"""Python

Estructuras de datos

Se trata de estructuras que permiten almacenar y organizar datos de manera eficiente.
En Python existen varias estructuras de datos, entre las más importantes se encuentran:
    - Listas
    - Tuplas
    - Diccionarios
"""

"""
Listas

Son estructuras de datos que permiten almacenar una colección de elementos, los cuales pueden ser de diferentes tipos de datos (enteros, cadenas, booleanos, etc.). Las listas son mutables, lo que significa que se pueden modificar después de su creación.
"""

lista = [1, 2, 3, 4, 5]
lista_2 = ["Hola", "Mundo", "!"]
lista_3 = [1, "Hola", 3.14, True]

lista_vacia = []

# Acceder a los elementos de una lista
print(f"Lista completa: {lista}")
print(f"Tercer elemento de la lista: {lista[2]}")

lista[2] = "manzana"
print(f"Lista modificada: {lista}")

# Métodos de listas

# append(): Agrega un elemento al final de la lista.
lista.append(6)
print(f"Lista después de append: {lista}")

# extend(): Agrega los elementos de otra lista al final de la lista.
lista.extend([7, 8, 9])
print(f"Lista después de extend: {lista}")

# insert(): Inserta un elemento en una posición específica de la lista.
lista.insert(2, "naranja")
print(f"Lista después de insert: {lista}")

# remove(): Elimina la primera aparición de un elemento en la lista.
lista.remove("naranja")
print(f"Lista después de remove: {lista}")

# pop(): Elimina y devuelve el elemento en una posición específica de la lista.
elemento_eliminado = lista.pop(2)
print(f"Elemento eliminado con pop: {elemento_eliminado}")
print(f"Lista después de pop: {lista}")

# index(): Devuelve el índice de la primera aparición de un elemento en la lista.
indice = lista.index(4)
print(f"Índice del elemento 4: {indice}")

# len(): Devuelve el número de elementos en la lista.
longitud = len(lista)
print(f"Longitud de la lista: {longitud}")

# count(): Devuelve el número de veces que un elemento aparece en la lista.
cantidad = lista.count(2)
print(f"Cantidad de veces que aparece el elemento 2: {cantidad}")

# sort(): Ordena los elementos de la lista en orden ascendente.
# Nota: Para ordenar de forma descentete, se puede utilizar: lista.sort(reverse=True)
lista.sort()
print(f"Lista después de sort: {lista}")

# reverse(): Invierte el orden de los elementos de la lista.
lista.reverse()
print(f"Lista después de reverse: {lista}")

# slice(): Permite obtener una sublista a partir de la lista original.
# Nota: El elemento de cierre no se incluye en la sublista.
sublista = lista[1:5]
print(f"Sublista obtenida con slice: {sublista}")

lista[1:5] = []
print(f"Lista después de eliminar elementos con slice: {lista}")

# clear(): Elimina todos los elementos de la lista.
lista.clear()
print(f"Lista después de clear: {lista}")


"""
Tuplas

Son estructuras de datos que permiten almacenar una colección de elementos, los cuales pueden ser de diferentes tipos de datos (enteros, cadenas, booleanos, etc.). A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
"""

tupla = (1, 2, 3, 4, 5)
print(f"Tupla completa: {tupla}")

# Acceder a los elementos de una tupla
print(f"Tercer elemento de la tupla: {tupla[2]}")

# Métodos de tuplas

# count(): Devuelve el número de veces que un elemento aparece en la tupla.
cantidad_tupla = tupla.count(2)
print(f"Cantidad de veces que aparece el elemento 2 en la tupla: {cantidad_tupla}")

# index(): Devuelve el índice de la primera aparición de un elemento en la tupla.
indice_tupla = tupla.index(4)
print(f"Índice del elemento 4 en la tupla: {indice_tupla}")

# len(): Devuelve el número de elementos en la tupla.
longitud_tupla = len(tupla)
print(f"Longitud de la tupla: {longitud_tupla}")


"""
Diccionarios

Son estructuras de datos que permiten almacenar una colección de elementos, los cuales están organizados en pares clave-valor. Las claves son únicas y se utilizan para acceder a los valores correspondientes. Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación.
"""

persona = {
    "nombre": "Elio",
    "edad": 20,
    "genero": "Masculino",
    "nacionalidad": "Venezolano",
    "hobbies": ["analizar datos", "leer", "beber café"]
}

# Acceder a los elementos de un diccionario
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")
print(f"Género: {persona['genero']}")
print(f"Nacionalidad: {persona['nacionalidad']}")
print(f"Hobbies: {persona['hobbies']}")

# Métodos de diccionarios

# keys(): Devuelve una lista con las claves del diccionario.
claves = persona.keys()
print(f"Claves del diccionario: {claves}")

# values(): Devuelve una lista con los valores del diccionario.
valores = persona.values()
print(f"Valores del diccionario: {valores}")

# items(): Devuelve una lista de tuplas, donde cada tupla contiene una clave y su valor correspondiente.
elementos = persona.items()
print(f"Elementos del diccionario: {elementos}")