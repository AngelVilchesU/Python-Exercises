"""
Ejercicio: Pide un número y comprueba si es par o impar usando if y módulo %

Lógica   : Usar input() e int() para el ingreso y validación del número, usar if y módulo para determinar
           si el valor es impar o no
"""

# Variables
num = int(input("Ingrese el valor a evaluar: "))

# Proceso
if num % 2 == 0: # Si no hay remanente es par
    print("Es par")
elif num % 2 != 0: # Si hay remanente es impar
    print("Es impar")

# Resultado

# ¿Cómo mejorar la lógica?

