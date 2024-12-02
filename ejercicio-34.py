"""
Ejercicio: Verifica si una cadena es mayor o igual a 10 caracteres

Lógica   : definir la cadena, usar len()  y condicionales para definir su es mayor o igual a 10 caracteres
"""

# Variables
string1 = "Los ogros son como cebollas"
string2 = "Mira Shrek"
string3 = "Pantano"
string4 = "Los botones no"
listaStr = []
listaStr.append(string1)
listaStr.append(string2)
listaStr.append(string3)
listaStr.append(string4)

# Proceso

# Resultado
for elem in listaStr:
    if len(elem) >= 10:
        print(f"El string '{elem}' tiene 10 o más caracteres")

# ¿Cómo mejorar la lógica?

