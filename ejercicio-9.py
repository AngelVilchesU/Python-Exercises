"""
Ejercicio: Realiza la potencia de un número

Lógica   : Definir variables numéricas (base y exponente) y usar operador potencia ** con función print()
"""

# Variables
base = 4.0
exponente = 2

# Proceso
pot = base ** exponente

# Resultado
print(f"{base} elevado a {exponente} es {pot}")

# ¿Cómo mejorar la lógica?
# Usar inputs y validadores

# O/F con librería
import math

print(math.pow(base, exponente))
