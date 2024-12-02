"""
Ejercicio: Crear programa que permita crear, leer y agregar información en un archivo txt
"""

# Variables
class Archivo:
    def __init__(self, nombre="", mensaje=""):
        self.nombre = nombre
        self.mensaje = mensaje

    def setNombre(self, nombre):
        self.nombre = nombre

    def setMensaje(self, mensaje):
        self.mensaje = mensaje

    def crearArchivo(self):
        with open(self.nombre, "w"):
            pass

    def agregarMensaje(self):
        with open(self.nombre, "w") as archivo:
            archivo.write(self.mensaje)

    def leerArchivo(self):
        with open(self.nombre, "r") as archivo:
            mensaje = archivo.read()
        return mensaje

archivo = Archivo()
archivo.setNombre("archivo.txt")
archivo.setMensaje("MI MENSAJE PERSONALIZADO")

# Proceso
archivo.crearArchivo()
print(archivo.leerArchivo())
archivo.agregarMensaje()
print(archivo.leerArchivo())

# Resultado


# ¿Cómo mejorar la lógica?

