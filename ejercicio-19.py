"""
Ejercicio: Cuenta las ocurrencias de un carácter específico en una cadena

Lógica   : Definir variable string, determinar carácter a evaluar, usar count para contar las
           ocurrencias
"""

# Variables
string = "Los ogros son como cebollas"
caracter = "o"

# Proceso
ocurrencias = string.count(caracter)

# Resultado
print(f"La cantidad de '{caracter}' son {ocurrencias}")

# ¿Cómo mejorar la lógica?
# Usar inputs, validadores y funciones
# Aplicar lower tanto al string como al caracter para contar todas las ocurrencias independiente
# ...sea mayús o minus (considerar que este es un caso donde la búsqueda no es éxacta)

# O/F sin count()
ocurrencias = 0
for carac in string:
    if carac == caracter:
        ocurrencias = ocurrencias + 1
print(f"La cantidad de '{caracter}' son {ocurrencias}")
