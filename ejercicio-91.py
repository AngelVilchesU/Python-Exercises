"""
Ejercicio: Filtrar números pares de una lista usando filter
"""

# Variables
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Proceso
esPar = lambda num: num % 2 == 0
pares = list(filter(esPar, lista))

# Resultado
print(pares)

# ¿Cómo mejorar la lógica?

