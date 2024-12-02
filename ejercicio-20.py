"""
Ejercicio: Encuentra y muestra el último carácter de una cadena

Lógica   : Definir string y mediante slicing extraer último carácter
"""

# Variables
string = "Los ogros son como cebollas"

# Proceso
ultimoCarac = string[-1::]

# Resultado
print("El último carácter es:", ultimoCarac)

# ¿Cómo mejorar la lógica?
# Agregar inputs, valdiadores y funciones

# O/F sin slicing
for carac in reversed(string):
    ultimoCarac = carac
    break
print("El último carácter es:", ultimoCarac)
