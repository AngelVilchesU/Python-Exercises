"""
Ejercicio: Invertir una cadena

Lógica   : Definir string, 
"""

# Variables
string = "cebollas"

# Proceso
string_inv = string[::-1]

# Resultado
print("La cadena inversa es:", string_inv)

# ¿Cómo mejorar la lógica?
# Usar inputs y validadores

# O/F manualmente
string_inv = ""
for char in reversed(string):
    string_inv = string_inv + char
print("O/F - La cadena inversa es:", string_inv)
