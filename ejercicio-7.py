"""
Ejercicio: Calcular promedio de una lista de números

Lógica   : Crear lista de números, usar sum() y len() para calcular el promedio y print()
"""

# Variables
lista = [1, 2, 3, 4, 5]

# Proceso
prom = sum(lista) / len(lista)

# Resultado
print("El promedio de los números de la lista es", prom)

# ¿Cómo mejorar la lógica?
# Validar que valores de la lista sean numéricos

# O/F sin usar sum() ni len()
suma = 0
largo = 0
for num in lista:
    suma = suma + num
    largo = largo + 1
prom = suma / largo
print("O/F - El promedio de los números de la lista es", prom)

# O/F con librería
from statistics import mean
prom = mean(lista)
print("O/F - El promedio de los números de la lista es", prom)
