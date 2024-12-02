"""
Ejercicio: Obten la cantidad de memoria ram en mi computador/laptop

Lógica   : Usar librería psutil
"""

import psutil

def fRam():
    mem = psutil.virtual_memory()
    return mem.total / (1024 ** 3)

# Variables


# Proceso


# Resultado
print(fRam())

# ¿Cómo mejorar la lógica?

