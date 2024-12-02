"""
Ejercicio: Filtrar cadenas que contienen un caracter especifico usando filter
"""

# Variables
lista = ["los", "ogros", "son", "como", "cebollas", "esta está excenta"]

# Proceso
tieneO = lambda string: "o" in string.lower()
res = list(filter(tieneO, lista))

# Resultado
print(res)

# ¿Cómo mejorar la lógica?

