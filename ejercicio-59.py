"""
Ejercicio: Pedir al usuario un número e imprimir la tabla de multiplicar del mismo

Lógica   : usar input() e int() para entrada y validación del número
           usar for y range con operador multiplicación para el resultado
"""

# Variables
num = int(input("Ingrese el número: "))

# Proceso
for i in range(0, 11):
    print(f"{num} x {i} = {num * i}")

# Resultado


# ¿Cómo mejorar la lógica?

