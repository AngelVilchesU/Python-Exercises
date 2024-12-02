"""
Ejercicio: Elimina un elemento específico de una lista

Lógica   : Definir lista, seleccionar elemento, mediante función remove() determinar su existencia
           y eliminarlo
"""

# Variables
lista = ["los", "ogros", "son", "como", "cebollas", "los", "ogros"]
elem = "los"

# Proceso
for item in lista:
    if item == elem:
        lista.remove(elem)

# Resultado
print(lista)

# ¿Cómo mejorar la lógica?
# Agregar inputs, validadores y funciones

# O/F sin remove
lista = [item for item in lista if item != elem]
print(lista)
