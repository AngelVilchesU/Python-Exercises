"""
Ejercicio: Simula el lanzamiento de un dado hasta obtener un 6

Lógica   : Crear un menú que permita volver a tirar (recordando que no se detiene hasta obtener 6)
           Usar random de 1 a 6 para determinar el valor de la cara
"""

import random

# Variables


# Proceso
while True:
    print("------------------------------")
    print("Ingrese '1' para tirar el dado")
    print("Ingrese '2' para salir")
    print("------------------------------")
    opcion = input("Ingrese la opción: ")

    if opcion == '1':
        dado = 0
        tiro = 1
        while dado != 6:
            dado = random.randint(1, 6)
            if dado == 6:
                print(f"Tiro {tiro} - FELICIDADES ha salido {dado}")
                break
            print(f"Tiro {tiro} - Ha salido {dado}")
            tiro = tiro + 1
    elif opcion == '2':
        print("Saliendo...")
        break
    else:
        print("Ingrese una opción válida")
# Resultado


# ¿Cómo mejorar la lógica?
# Usar case
# Eliminar contenido por consola anterior para evitar saturación de información por consola
