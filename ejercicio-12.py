"""
Ejercicio: Convierte un número entero en cadena

Lógica   : Definir variable numérica, usar función str() para transformalo en string y usar
           print() con type() para validar el tipo de dato 
"""

# Variables
numF = 2.1
numI = 2
print(f"El número flotante es {numF} y es del tipo {type(numF)}")
print(f"El número entero es {numI} y es del tipo {type(numI)}")

# Proceso
numFaStr = str(numF)
numIaStr = str(numI)

# Resultado
print(f"El número flotante CONVERTIDO es {numFaStr} y es del tipo {type(numFaStr)}")
print(f"El número entero CONVERTIDO es {numIaStr} y es del tipo {type(numIaStr)}")

# ¿Cómo mejorar la lógica?
# Utilizar inputs y validadores de entrada
# Usar funciones (def) para hacer el proceso
