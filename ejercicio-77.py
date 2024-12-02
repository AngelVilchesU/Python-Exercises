"""
Ejercicio: Crear clase Persona con atributos: nombre y edad; Métodos: constructor (datos pueden estar vacios),
            getters y setters, mostrarDatos() y esMayorDeEdad()

Lógica   : POO
"""

# Variables
class Persona:
    def __init__(self, nombre=None, edad=None):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nuevaEdad):
        self._edad = nuevaEdad

    def mostrarDatos(self):
        return self.__dict__
    
    def esMayorDeEdad(self):
        if self._edad >= 18:
            return True
        return False

# Proceso
persona1 = Persona("Matías", 19)
persona2 = Persona("Iván", 18)
persona3 = Persona("Ángel", 17)

# Resultado
print(persona1.mostrarDatos())
print(persona1.esMayorDeEdad())

print(persona2.mostrarDatos())
print(persona2.esMayorDeEdad())

print(persona3.mostrarDatos())
print(persona3.esMayorDeEdad())

# ¿Cómo mejorar la lógica?

