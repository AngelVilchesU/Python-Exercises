"""
Ejercicio: Imprimir la suma de los números pares del 1 al 10 con ciclo for

Lógica   : Usar range() con for junto con módulo para determinar paridad y una variable suma iterativa
"""

# Variables
sum = 0

# Proceso
for i in range(1, 11):
    if i % 2 == 0: # Es par
        sum = sum + i

# Resultado
print(sum)

# ¿Cómo mejorar la lógica?

