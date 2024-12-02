"""
Ejercicio: Genera una lista de números del 1 al 100

Lógica   : Usar range para generar números del 1 al 100 y, si lo permite, crear la lista
           con los 100 elementos a partir de range o, crear una lista y con un ciclo generar
           100 números y agregarlos a la lista
"""

# Variables
lista = list(range(1, 101))

# Proceso N/a

# Resultado
print(lista)

# ¿Cómo mejorar la lógica?
# Agregar inputs, validadores y funciones

# O/F sin range
lista = []
for i in range(100):
    lista.append(i + 1)
print(lista)
