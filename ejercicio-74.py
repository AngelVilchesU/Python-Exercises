"""
Ejercicio: Crear clase Persona con atributos: nombre, edad, dni
           Métodos: init(), es_mayor_de_edad()

Lógica   : POO
"""

# Variables
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return "Si" # O True
        return "No" # O False

# Proceso
persona1 = Persona("Matías", 19, 11111111111)
persona2 = Persona("Iván", 18, 22222222222)
persona3 = Persona("Ángel", 17, 33333333333)

# Resultado
print(f"Persona 1:\n{persona1.__dict__}\n¿Es mayor de edad? {persona1.es_mayor_de_edad()}")
print(f"Persona 2:\n{persona2.__dict__}\n¿Es mayor de edad? {persona2.es_mayor_de_edad()}")
print(f"Persona 3:\n{persona3.__dict__}\n¿Es mayor de edad? {persona3.es_mayor_de_edad()}")

# ¿Cómo mejorar la lógica?

