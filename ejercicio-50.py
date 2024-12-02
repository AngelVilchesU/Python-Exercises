"""
Ejercicio: Mostrar los número del 1 al 100, pero reemplazando los múltiplos de 3 por "Fizz" y los
           múltiplos de 5 por "Buzz"

Lógica   : Usar modulo de 3 y 5 según corresponda, valores múltiplos de 3 Y 5 serán "Fizz Buzz"
"""

# Variables
inicio = 1
fin = 100

# Proceso
while inicio <= fin:
    if inicio % 3 == 0 and inicio % 5 == 0: # Múltiplo de 3 Y 5
        print("Fizz Buzz")
    elif inicio % 3 == 0:
        print("Fizz")
    elif inicio % 5 == 0:
        print("Buzz")
    else:
        print(inicio)
    inicio = inicio + 1

# Resultado


# ¿Cómo mejorar la lógica?
# Usar case
# Eliminar contenido por consola anterior para evitar saturación de información por consola
