"""
Ejercicio: Imprime la tabla de multiplicar de un número ingresado por el usuario

Lógica   : Input() e int() para el ingreso y validación de la entrada numérica y operador *
"""

# Variables
num = int(input("Ingrese el valor: "))
limite = 10
i = 0

# Proceso
while i <= 10:
    print(f"{num} x {i} = {num * i}") 
    i = i + 1

# Resultado

# ¿Cómo mejorar la lógica?
# Usar formato de valores para mantener orden
