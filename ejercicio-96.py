"""
Ejercicio: Crear excepción que me ayude a determinar si el indice de una lista está fuera de rango
"""

# Variables
lista = [1, 2, 3, 4, 5]

# Proceso
try:
    print(lista[100])
except:
    print("Fuera de rango")

# Resultado
