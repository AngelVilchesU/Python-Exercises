"""
Ejercicio: Hacer un menú de opciones que incluya la opción de salir del programa

Lógica   : Crear un menú mediante ciclo while con input() y condicionales
"""

# Variables


# Proceso
while True:
    print("----------------------------------")
    print("Ingrese '1' para obtener mensaje 1")
    print("Ingrese '2' para obtener mensaje 2")
    print("Ingrese '3' para salir")
    print("----------------------------------")
    opcion = input("Ingrese la opción: ")
    if opcion == '1':
        print("Hola Shrek")
    elif opcion == '2':
        print("Los ogros son como cebollas")
    elif opcion == '3':
        print("Saliendo...")
        break
    else:
        print("Ingrese una opción válida")

# Resultado

# ¿Cómo mejorar la lógica?
# Usar case en lugar de condicionales
# Eliminar contenido por consola anterior para evitar saturación de información por consola
