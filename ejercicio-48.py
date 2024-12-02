"""
Ejercicio: Simular un lanzamiento de moneda

Lógica   : Usar random para generar valores 0 o 1 (cara o cruz) más un menú (lanzar moneda o salir)
"""

import random
import time

# Variables


# Proceso
while True:
    print("------------------------------------")
    print("Ingrese '1' para lanzar la moneda")
    print("Ingrese '2' para salir del programa")
    print("------------------------------------")
    opcion = input("Ingrese la opción seleccionada: ")

    if opcion == '1':
        print("Lanzando moneda...")
        time.sleep(3)
        # Lógica de lanzamiento
        caraOcruz = random.randint(0, 1)
        if caraOcruz == 0: # CARA
            print("Salió cara")
        elif caraOcruz == 1: # CRUZ
            print("Salió cruz")
    elif opcion == '2':
        print("Saliendo...")
        time.sleep(3)
        break
    else:
        print("Ingrese una opción válida")

# Resultado

# ¿Cómo mejorar la lógica?
# Usar case
# Eliminar contenido por consola anterior para evitar saturación de información por consola

