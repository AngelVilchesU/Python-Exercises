"""
Ejercicio: Escribe una función que pida al usaurio distancia y velocidad para calcular tiempo de viaje

Lógica   : Usar def() y operador división / entre distancia y velocidad
"""

def fTiempo(distancia, velocidad):
    return round(distancia / velocidad, 3)

# Variables
distancia = float(input("Ingrese la distancia en km: "))
velocidad = float(input("Ingrese la distancia en km/h: "))

# Proceso
tiempo = fTiempo(distancia, velocidad)

# Resultado
print(f"El tiempo de viaje con distancia {distancia} KM a una velocidad de {velocidad} KM/H es de {tiempo} H")

# ¿Cómo mejorar la lógica?
# Abarcar más unidades de tiempo/distancia, o la conversión de unidades
