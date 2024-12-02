# Entrada: String
# Elimina caracteres duplicados consecutivos en una cadena, espacios al inicio y al final de la cadena y cualquier signo de !, ,, . o
# capitaliza la primera letra de cada palabra

def fEliminarEspaciosInFn(string):
    return string.strip()
        
def fEliminarCaracteres(string):
    caracteresEspeciales = "!,.$"
    for char in caracteresEspeciales:
        string = string.replace(char, "")
    return string
        
def fEliminarDuplicados(string):
    stringF = ""
    prevChar = ""
    for char in string:
        if prevChar != char:
            stringF = stringF + char
            prevChar = char
    return stringF

def fCapitalizarPalabra(string):
    return string.title()

string = " Laaattaam$mm airliness By! ,me...     " # Respuesta: "Latam Airlines By Me"
string = fEliminarEspaciosInFn(string)
string = fEliminarCaracteres(string)
string = fEliminarDuplicados(string)
string = fCapitalizarPalabra(string)

print(f"<{string}>")
