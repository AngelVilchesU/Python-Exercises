"""
Ejercicio: Combina dos listas en pares usando la función zip()

Lógica   : Definir dos listas y usar función zip() dentro de un list()
"""

# Variables
lista1 = ["Shrek", "Shrek", "Shrek"]
lista2 = [1, 2, 3]

# Proceso
res = list(zip(lista1, lista2))

# Resultado
print(res)

# ¿Cómo mejorar la lógica?

# O/F con ciclos
res = []
largoLista1 = len(lista1)
largoLista2 = len(lista2)
if largoLista1 == largoLista2:
    i = 0
    while i < largoLista1:
        tupla = (lista1[i], lista2[i])
        res.append(tupla)
        i = i + 1
print(res)
