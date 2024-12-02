"""
Ejercicio: Verifica si una cadena es un palíndromo

Lógica   : Definir string, revertirlo con slicing y comparar con condicionales 
"""

# Variables
string1 = "ogro"
string2 = "radar"

# Proceso
string1Rev = string1[::-1]
string2Rev = string2[::-1]

# Resultado
if string1 == string1Rev:
    print("String 1 es palíndromo")
else:
    print("String 1 NO es palíndromo")
if string2 == string2Rev:
    print("String 2 es palíndromo")
else:
    print("String 2 NO es palíndromo")

# ¿Cómo mejorar la lógica?
# Usar inputs, validadores y funciones

# O/F sin slicing
string1Rev = ""
string2Rev = ""

for carac in reversed(string1):
    string1Rev = string1Rev + carac
for carac in reversed(string2):
    string2Rev = string2Rev + carac
if string1 == string1Rev:
    print("String 1 es palíndromo")
else:
    print("String 1 NO es palíndromo")
if string2 == string2Rev:
    print("String 2 es palíndromo")
else:
    print("String 2 NO es palíndromo")
