"""
Ejercicio: Gerera un número aleatorio entre 1 y 10. Luego, pide al usuario adivinar el número hasta
           que lo haga correctamente

Lógica   : Utilizar librería random para generar el número y ciclos para que el usuario adivine
"""

import random

# Variables
respuesta = random.randint(1, 10)
numero_usuario = -1

# Proceso
while True:
    try:
        numero_usuario = int(input("Ingrese el número: "))
    except:
        print("Solo ingrese números enteros")
    if numero_usuario == respuesta:
        print("Correcto")
        break
    print("Número equivocado, intentalo nuevamente")

# Resultado

# ¿Cómo mejorar la lógica?
# Agregar limite de intentos
