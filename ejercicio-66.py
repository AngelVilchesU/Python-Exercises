"""
Ejercicio: Escribe una función para calcular el promedio de una lista de número

Lógica   : usar def(), sum() y len() para calcular promedio o mean() de la librería statistics
"""

def fPromedio(lista):
    return sum(lista) / len(lista)

# Variables
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Proceso
res = fPromedio(lista)

# Resultado
print(res)

# ¿Cómo mejorar la lógica?
# Usar librería
# Validar valores numéricos

# O/F con statistics
from statistics import mean
res = 0
res = mean(lista)
print(res)
