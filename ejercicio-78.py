"""
Ejercicio: Crear clase Persona y otra Estudiante
           La clase Persona tiene atributo nombre y método mostrarNombre
           La clase Estudiante debe heredar de la clase Persona atributos y métodos

Lógica   : POO
"""

# Variables
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrarNombre(self):
        return f"Nombre: {self.nombre}"
    
class Estudiante(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def mostrarNombre(self):
        return super().mostrarNombre()

# Proceso
estudiante1 = Estudiante("Iván")

# Resultado
print(estudiante1.mostrarNombre())

# ¿Cómo mejorar la lógica?

