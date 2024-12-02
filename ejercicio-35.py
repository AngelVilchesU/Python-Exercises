"""
Ejercicio: Comprueba si un número está en el rango del 1 al 100

Lógica   : Usar operadores de comparación e if
"""

# Variables
lista = [1, 99, 0, 100, 101, 50, 999]

# Proceso
for num in lista:
    if num >= 1 and num <= 100:
        print(f"El número {num} está entre el 1 y el 100")
    else:
        print(f"El número {num} NO está entre el 1 y el 100")

# Resultado

# ¿Cómo mejorar la lógica?
