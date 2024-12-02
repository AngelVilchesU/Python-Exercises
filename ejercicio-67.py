"""
Ejercicio: Escribe una función para calcular el volumen de un cilindro V=pi*r^2h

Lógica   : Usar math() y def()
"""

import math

def fCilindroVolumen(radio, altura):
    return round(math.pi * radio ** 2 * altura, 2)

# Variables
radio = 3
altura = 5

# Proceso
res = fCilindroVolumen(radio, altura)

# Resultado
print(res)

# ¿Cómo mejorar la lógica?

