"""
Ejercicio: Solicita al usuario un número N y luego imprime la suma de todos los números desde el 1 hasta N

Lógica   : Usar input() y int() para ingresar y validar entrada numérica, mediante un ciclo sumar en una
           variable iterativa los números de 1 a N
"""

# Variables
n = int(input("Ingrese el valor N: "))

# Proceso
iter = 0
for i in range(n + 1): # + 1 porque es < y no <=
    iter = iter + i

# Resultado
print(iter)

# ¿Cómo mejorar la lógica?
# Abarcar número flotantes
