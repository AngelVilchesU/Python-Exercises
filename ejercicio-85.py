"""
Ejercicio: Contar el número de vocales en una lista de palabras

Lógica   : usar map(), ciclos y condicionales
"""

VOCALES = ["a", "e", "i", "o", "u"]

def contadorVocales(string):
    contador = 0
    for char in string:
        if char.lower() in VOCALES:
            contador = contador + 1
    return contador



# Variables
lista = ["los", "Ogros", "son", "cOmo", "CebollAs"]

# Proceso
totalVocales = list(map(contadorVocales, lista))

# Resultado
print(lista)
print(totalVocales)

# ¿Cómo mejorar la lógica?

