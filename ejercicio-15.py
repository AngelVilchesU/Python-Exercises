"""
Ejercicio: Ordena una lista de números de mayor a menor

Lógica   : Definir variable list() con valores numéricos y utilizar función sort() para ordenar
"""

# Variables
lista = [5, 4, 3, 2, 1, 6, 7, 8, 9]

# Proceso
lista.sort()

# Resultado
print(lista)

# ¿Cómo mejorar la lógica?
# Usar inputs y validadores de entrada

# O/F sin Sort y con Bubblesort
lista = [1, 2, 3, 2, 1, 6, 7, 8, 9]
listaLargo = len(lista)
for i in range(listaLargo):
    intercambio = False # Variable para verificar si hubo intercambio de valores
    for j in range(0, listaLargo - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j] # Intercambio
            intercambio = True # Hubo intercambio
    if not intercambio:
        break
print(lista)

# Adicional
lista.sort(reverse=True)
print(lista)

# Adicional 2 
lista = [1, 2, 3, 2, 1, 6, 7, 8, 9]
listaLargo = len(lista)
for i in range(listaLargo):
    intercambio = False # Variable para verificar si hubo intercambio de valores
    for j in range(0, listaLargo - i - 1):
        if lista[j] < lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j] # Intercambio
            intercambio = True # Hubo intercambio
    if not intercambio:
        break
print(lista)
