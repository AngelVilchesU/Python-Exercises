"""
Ejercicio: Convertir una lista de cadenas de números a enteros 

Lógica   : usar map(), también se puede usar ciclos
"""

def conversor(numStr):
    return int(numStr)

# Variables
listaCadenas = ["1", "2", "3", "4", "5"]

# Proceso
listaEnteros = list(map(conversor, listaCadenas))

# Resultado
for num in listaEnteros:
    print(f"Número {num} del tipo {type(num)}")

# ¿Cómo mejorar la lógica?

