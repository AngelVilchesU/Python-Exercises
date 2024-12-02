"""
Ejercicio: Escribe una función para calcular la tasa de desempleo
           td = no_desempleados / fuerza_laboral * 100
Lógica   : 
"""

def fTasaDesempleo(noEmpleados, totalEmpleados):
    return round(noEmpleados / totalEmpleados * 100, 2)

# Variables
noEmpleados = 10
totalEmpleados = 100

# Proceso
res = fTasaDesempleo(noEmpleados, totalEmpleados)

# Resultado
print(f"{res} %")

# ¿Cómo mejorar la lógica?

