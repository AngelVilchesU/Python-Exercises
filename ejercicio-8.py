"""
Ejercicio: Crea una tupla con elementos e imprimirla

Lógica   : Crear variable tuple() o () con distintos (o no) elementos y usar función print()
"""

# Variables
tupla = (1, 2.0, False, "cebolla")

# Proceso N/A

# Resultado
print("La tupla es:", tupla)

# ¿Cómo mejorar la lógica?
# Imprimir elementos con ciclo para que no figuren parentésis

# O/F con ciclo
for elem in tupla:
    print(elem, " ", end="")
