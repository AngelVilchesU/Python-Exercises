"""
Ejercicio: Crear clase animal con atributos especie y nombre. Metodos init y hablar()

Lógica   : POO
"""

# Variables
class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

    def hablar(self):
        if self.especie == 'perro':
            return "GUAU!"
        elif self.especie == 'gato':
            return "MIAU!"

# Proceso
animal1 = Animal("perro", "Bobby")
animal2 = Animal("gato", "Michi")

# Resultado
print(animal1.__dict__)
print(animal1.hablar())
print("--------------------------------------")
print(animal2.__dict__)
print(animal2.hablar())

# ¿Cómo mejorar la lógica?

