"""
Ejercicio: Escribe una función para convertir grados celsius a fahrenheit

Lógica   : 
"""

def fCelsiusAFahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

# Variables
celsius = float(input("Ingrese los grados celsius: "))

# Proceso
fahrenheit = fCelsiusAFahrenheit(celsius)

# Resultado
print(fahrenheit)

# ¿Cómo mejorar la lógica?

