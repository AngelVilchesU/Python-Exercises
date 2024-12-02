"""
Ejercicio: Crear clase Libro
           Atributos: titulo, autor, editorial y año de publicación
           Métodos: constructor para inicializar atributos

Lógica   : POO
"""

# Variables
class Libro:
    def __init__(self, titulo, autor, editorial, anioPublicacion):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anioPublicacion = anioPublicacion

# Proceso
libro1 = Libro("Aprender python programando", "No recuerdo", "No lo sé", "Tampoco lo recuerdo")

# Resultado
print(f"Libro\nTitulo: {libro1.titulo}\nAutor: {libro1.autor}\nEditorial: {libro1.editorial}\nAño de publicación: {libro1.anioPublicacion}")

# ¿Cómo mejorar la lógica?

# O/F de print
print(libro1.__dict__)
