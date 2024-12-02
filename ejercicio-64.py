"""
Ejercicio: Escribe una función para verificar si un número es par o impar

Lógica   : usar módulo % de 2 para validar
"""

def fPar(num):
    if num % 2 == 0: # Par
        return True
    return False

# Variables
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Proceso
for elem in lista:
    esPar = fPar(elem)
    if esPar:
        print(f"El número {elem} es par")
    else:
        print(f"El número {elem} es impar")


# Resultado


# ¿Cómo mejorar la lógica?
# Validar si entra un digito y no un string o algo más no deseado
