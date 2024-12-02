"""
Ejercicio: Verífique si la palabra ingresada es python

Lógica   : Usar input() y str() para la entrada y validación. Usar lower() para abarcar más casos de uso
           y operador comparador con if para determinar igualdad. También borrar espacios en blanco
"""

# Variables
string = str(input("Ingrese la palabra: "))
palabra = "python"

# Proceso
string = string.replace(" ", "")

if string.lower() == palabra:
    print("La palabra ingresada es 'python'")
else:
    print("La palabra ingresada NO es 'python'")

# Resultado

# ¿Cómo mejorar la lógica?

