"""
Ejercicio: Elevar al cuadrado una lista de números

Lógica   : usar map(), también se puede usar ciclos
"""

def NumAlCuadrado(num):
    return num ** 2

# Variables
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Proceso
listaCuadrados = list(map(NumAlCuadrado, lista))

# Resultado
print(listaCuadrados)

# ¿Cómo mejorar la lógica?

