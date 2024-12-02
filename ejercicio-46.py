"""
Ejercicio: Solicita al usuario ingresar un número y cuenta cuántos digitos tiene

Lógica   : Usar input() e int() para el ingreso del número, luego con len() y str() el número de digitos
"""

# Variables
num = int(input("Ingrese el valor a evaluar: "))

# Proceso
largoNum = len(str(num))

# Resultado
print(largoNum)

# ¿Cómo mejorar la lógica?
# Abarcar decimales a partir de la coma ',' empleando split para dividir entre enteros y decimales
# Agregar try except dentro de un ciclo para evitar error de programa no controlado

# O/F son len(str())
contador = 0
while num != 0:
    num = num // 10
    contador = contador + 1
print(contador)
