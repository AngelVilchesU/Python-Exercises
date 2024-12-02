"""
Ejercicio: Crear una clase Circulo con los siguientes atributos: radio
           La clase debe tener los siguientes métodos: calcular_area - calcular_perimetro

Lógica   : POO
"""

import math

# Variables
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return round(math.pi * self.radio ** 2, 3)
    
    def calcular_perimetro(self):
        return round(2 * math.pi * self.radio, 3)

# Proceso
circulo1 = Circulo(5)

# Resultado
print(f"Área: {circulo1.calcular_area()} - Perimetro: {circulo1.calcular_perimetro()}")

# ¿Cómo mejorar la lógica?

