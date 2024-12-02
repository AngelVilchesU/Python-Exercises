# BubbleSort
lista1 = [5, 3.14, 2, 9.81, 7, 1.61, 8, 2.71, 3, 4, 6, 10, 1.41, 7.77, 11, 13, 0.99, 15.9, 19, 21.5]
lista2 = [21, 0.5, 7, 11, 14.3, 19, 13, 17, 5, 6.28, 9, 8.77, 2.5, 1, 4, 15.1, 3.3, 20, 18, 16]

def bubbleSort(lista):
    largo = len(lista)
    for i in range(largo):
        for j in range(largo - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista    

lista1 = bubbleSort(lista1)
lista2 = bubbleSort(lista2)

print(lista1)
print(lista2)
