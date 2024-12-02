"""
Ejercicio: Filtrar elementos que son listas
"""

# Variables
lista = ["No es lista", 12, ["lista", "de", "listas"], [], [2]]

# Proceso
esLista = lambda elem: isinstance(elem, list)
res = list(filter(esLista, lista))

# Resultado
print(res)

# ¿Cómo mejorar la lógica?
