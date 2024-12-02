"""
Ejercicio: Escribir en un html un mensaje
"""

def escribirArchivo(nombre, mensaje):
    with open(nombre, "w") as archivo:
        archivo.write(mensaje)

# Variables
mensaje = "Gracias Facultad Autodidacta!"
nombre = "index.html"

# Proceso


# Resultado
escribirArchivo(nombre, mensaje)

# ¿Cómo mejorar la lógica?

