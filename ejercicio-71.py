"""
Ejercicio: Crear clase Rectangulo con siguientes atributos:
            base: base del rectángulo
            altura: altura del rectángulo
           La clase debe tener los siguientes métodos:
            ** __init__(self, base, altura): inicializa los atributos de la clase
            ** calcular_area(self): calcula y devuelve el área del rectángulo
            ** calcular_perimetro(self): calcula y devuelve el perimetro del rectángulo

Lógica   : POO
"""

# Variables
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Proceso
rectangulo1 = Rectangulo(5, 3)

# Resultado
print(f"Área: {rectangulo1.calcular_area()} - Perimetro: {rectangulo1.calcular_perimetro()}")

# ¿Cómo mejorar la lógica?

