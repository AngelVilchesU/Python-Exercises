"""
Ejercicio: Pide un número y verifica si es positivo, negativo o neutro

Lógica   : USar input() para el ingreso del número, si es mayor a 0 es positivo, si es menor negativo y
           si es 0 es neutro (operadores < > ==)
"""

# Variables
num = float(input("Ingrese el número a evaluar: "))

# Proceso
if num == 0:
    print("El número es neutro")
elif num < 0:
    print("El número es negativo")
elif num > 0:
    print("El número es positivo")

# Resultado

# ¿Cómo mejorar la lógica?

