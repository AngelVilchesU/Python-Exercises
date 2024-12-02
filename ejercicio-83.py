"""
Ejercicio: Calcular la longitud de una lista de palabras

Lógica   : usar map(), len() o ciclos
"""

def longitudLista(string):
    return len(string)

# Variables
listaStrings = ["Los", "Ogros", "Son", "Como", "Cebollas"]

# Proceso
longitud = list(map(longitudLista, listaStrings))

# Resultado
print(listaStrings)
print(longitud)

# ¿Cómo mejorar la lógica?

