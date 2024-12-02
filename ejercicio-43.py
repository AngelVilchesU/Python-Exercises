"""
Ejercicio: Solicita al usuario ingresar un número n e imprime el factorial de ese número

Lógica   : 
"""

# Variables
n = int(input("Ingrese el valor N: "))
factorial = 1
i = 1

# Proceso
while i <= n:
    factorial = factorial * i
    i = i + 1

# Resultado
print(factorial)

# ¿Cómo mejorar la lógica?
# Usar recursividad
