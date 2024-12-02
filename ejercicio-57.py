"""
Ejercicio: imprimir los números del 1 al 5 en orden descendente

Lógica   : usar range() y reverse()
"""

# Variables


# Proceso
for i in reversed(range(1, 6)):
    print(i, " ", end="")

# Resultado


# ¿Cómo mejorar la lógica?

# O/F
print("")
for i in range(5, 0, -1):
    print(i, " ", end="")
