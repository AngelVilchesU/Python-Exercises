"""
Ejercicio: Crear lista con diferentes elementos e imprimirla

Lógica   : Crear variable list() ([]) y agregar elementos como int, float, boolean y string, e
           imprimirla con función print()
"""

# Variables
lista = [1, 1.512, True, "oGrO"]

# Proceso (No aplica)

# Resultado
print(lista)

# ¿Cómo mejorar la lógica?
# Imprimir lista por elementos con ciclo en una línea para que no figuren los corchetes

# O/F
for elem in lista:
    print(elem, " ", end="")
