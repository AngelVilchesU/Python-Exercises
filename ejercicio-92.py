"""
Ejercicio: Filtrar cadenas de longitud mayor que 3 de una lista usando filter
"""

# Variables
lista = ["1", "11", "111", "1111", "9", "999999999999", "ogros"]

# Proceso
esMayorQueTres = lambda string: len(string) > 3
res = list(filter(esMayorQueTres, lista))

# Resultado
print(res)

# ¿Cómo mejorar la lógica?

