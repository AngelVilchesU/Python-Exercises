"""
Ejercicio: Elimina duplicados de una lista

Lógica   : Usar set() para crear un conjunto que por defecto no tiene duplicados y luego transformarlo a list()
"""

# Variables
lista = [1, 1, 2, 3, 4, 5, 5, 6, 7,7,7,7,7,7, 1, 8, 9]

# Proceso
lista = list(set(lista))

# Resultado
print(lista)

# ¿Cómo mejorar la lógica?

# O/F (otra forma)
listaOF = []
for elem in lista:
    if elem not in listaOF:
        listaOF.append(elem)
print(listaOF)
