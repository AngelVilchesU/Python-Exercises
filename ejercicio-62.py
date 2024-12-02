"""
Ejercicio: Crea una función para calcular el área de un círculo

Lógica   : 
"""

import math

def fArea(radio):
    return math.pi * (radio ** 2)

# Variables
radio = float(input("Ingrese el radio del círculo: "))

# Proceso
res = round(fArea(radio), 2)

# Resultado
print("El área es:", res)

# ¿Cómo mejorar la lógica?

