"""
Ejercicio: Crear cadena de texto y mostrar su longitud

Lógica   : Crear variable string, usar función len() y print()
"""

# Variables
string = "Los ogros son como cebollas"

# Proceso
string_len = len(string)

# Resultado
print(f"El largo de la cadena de texto es de {string_len} caracteres (incluidos espacios)")

# ¿Cómo mejorar la lógica?
# Permitir opción de no contar espacios vacios

# O/F sin len()
string_len = 0
for carac in string:
    string_len = string_len + 1
print(f"O/F - El largo de la cadena de texto es de {string_len} caracteres (incluidos espacios)")
