"""
Ejercicio: Escribe una función para clasificar si una sustancia es ácida, básica o neutra a partir de su pH

Lógica   : ph<7 = ácida - ph>7 = básica - ph=7 = neutra
"""

def fClasificador(ph):
    if ph < 7:
        print("La sustancia es ácida")
    elif ph > 7:
        print("La sustancia es básica")
    elif ph == 7:
        print("La sustancia es neutra")
    else:
        print("No válido")

# Variables
ph = int(input("Ingrese el pH: "))

# Proceso

# Resultado
fClasificador(ph)

# ¿Cómo mejorar la lógica?

