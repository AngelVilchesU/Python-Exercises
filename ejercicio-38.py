"""
Ejercicio: Determina si un número es divisble entre 5 y 7

Lógica   : Usar operador módulo para determinar si es divisible por ambos números
"""

# Variables
lista = [1, 5, 7, 14, 35]
div1 = 5
div5 = 7

# Proceso
for num in lista:
    if num % 5 == 0 and num % 7 == 0:
        print(f"El número {num} es divisible por 5 y 7")
    else:
        print(f"El número {num} NO es divisible por 5 y 7")

# Resultado

# ¿Cómo mejorar la lógica?

