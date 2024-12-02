"""
Ejercicio: Crear una clase coche con los atributos: marca, modelo, matricula, km
           Métodos: init() - avanzar(km) que aumenta los km

Lógica   : POO
"""

# Variables
class Coche:
    def __init__(self, marca, modelo, matricula, km):
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.km = km

    def avanzar(self, km):
        self.km = self.km + km

# Proceso
coche1 = Coche("Marca 1", "Modelo 1", "Matrocula 1", 10)

# Resultado
print(coche1.__dict__)
coche1.avanzar(90)
print(coche1.__dict__)

# ¿Cómo mejorar la lógica?

