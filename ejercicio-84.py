"""
Ejercicio: Obtener el cuadrado de la suma de dos listas de números usando map()
"""

def sumaAlCuadrado(num1, num2):
    return (num1 + num2) ** 2

# Variables
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

# Proceso
cuadrados = list(map(sumaAlCuadrado, lista1, lista2))


# Resultado

print(cuadrados)

# ¿Cómo mejorar la lógica?

