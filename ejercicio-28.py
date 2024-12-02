"""
Ejercicio: Extrae un elemento específico de una tupla

Lógica   : Definir la tupla y mediante index o un ciclo  extraer el elemento
"""

# Variables
tupla = (1, 2, 3, 4, 5)

# Proceso
elem = tupla[0]

# Resultado
print(elem)

# ¿Cómo mejorar la lógica?

# O/F con elemento específico sin posición
elem = 1 # reset
res = ""
for item in tupla:
    if elem == item:
        res = item 
        break
print(elem)
