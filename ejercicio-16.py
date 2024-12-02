"""
Ejercicio: Calcula 2 elevado a la 4ta potencia sin usar operador **

Lógica   : Definir variables numéricas, importar librería math y utilizar función pow()
"""

# Librerías
from math import pow

# Variables
base = 2
potencia = 4

# Proceso
res = pow(base, potencia)

# Resultado
print(res)

# ¿Cómo mejorar la lógica?
# Usar inputs, validadores y funciones

# O/F sin pow ni operador **
res = 0
for i in range(potencia):
    res = res + (base * base)
print(res)
