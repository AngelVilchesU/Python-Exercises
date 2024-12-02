"""
Ejercicio: Filtrar números negativos de una lista utilizando filter
"""

# Variables
lista = [-10, -5, -1, 0, 3, 7, 12]

# Proceso
esNegativo = lambda num: num < 0
res = list(filter(esNegativo, lista))

# Resultado
print(res)

# ¿Cómo mejorar la lógica?

