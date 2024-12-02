"""
Ejercicio: Crear una función para sumar dos números

Lógica   : Usar def() que reciba dos entradas numéricas y sumarlas con operador +
"""

def fSuma(num1, num2):
    return num1 + num2

# Variables
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Proceso
res = fSuma(num1, num2)

# Resultado
print(f"{num1} + {num2} = {res}")

# ¿Cómo mejorar la lógica?
# Agregar try except en caso de no ingresar entrada correcta (número) y/o ciclo while con validadores
