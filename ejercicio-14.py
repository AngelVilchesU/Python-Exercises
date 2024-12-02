"""
Ejercicio: Pasa una cadena de mayúsculas a minúsculas

Lógica   : Definir variable string y utilizar función lower()
"""

# Variables
string = "LOS OGROS SON COMO CEBOLLAS"
print(string)

# Proceso
string = string.lower()

# Resultado
print(string)

# ¿Cómo mejorar la lógica?
# Usar inputs y validadores
# Añadir función para volver a mayúsculas
# Solo dejar mayúscula la primera letra

# Adicional
string = string.upper()[0:1:] + string[1::]
print("Adicional:", string)
