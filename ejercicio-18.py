"""
Ejercicio: Convierte un número décimal a un número entero

Lógica   : Crear variable numérica float() y luego usar int() para convertirla en entera.
           Usar type() para validar el tipo de dato
"""

# Variables
decimal = 2.6
print(f"Valor {decimal} del tipo {type(decimal)}")

# Proceso
entero = int(decimal)

# Resultado
print(f"Valor {entero} del tipo {type(entero)}")

# ¿Cómo mejorar la lógica?
# Agregando inputs, validadores y funciones
# Posibilidad de redondear al entero más cercano y no al entero menor

# O/F redondear al entero más cercano
entero = int(round(decimal))
print(f"Valor {entero} del tipo {type(entero)}")
