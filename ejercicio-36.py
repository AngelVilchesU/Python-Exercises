"""
Ejercicio: Pide un caracter y determina si es vocal

Lógica   : Usar input() y str() para la entrada y validación del dato y lower para abarcar más casos
           con if para comparar
"""

# Variables
while True:
    char = str(input("Ingrese el caracter: "))
    if len(char) == 1:
        break
vocales = ['a', 'e', 'i', 'o', 'u']

# Proceso
if char.lower() in vocales:
    print(f"El caracter '{char}' es una vocal")
else:
    print(f"El caracter '{char}' NO es una vocal")

# Resultado

# ¿Cómo mejorar la lógica?

