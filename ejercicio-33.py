"""
Ejercicio: Determina si un año es bisiesto  
            Reglas:
                - Divisible por 4
                - No divisible por 100
                - Divisible por 400

Lógica   : 
"""

# Variables
anio = int(input("Ingrese el año a evaluar: "))

# Proceso
div4 = anio % 4
div100 = anio % 100
div400 = anio % 400

# Resultado
if (div4 == 0 and div100 != 0) or (div400 == 0 and div100 != 0): # No hay remanente
    print("Es bisiesto")
else:
    print("No es bisiesto")

# ¿Cómo mejorar la lógica?

