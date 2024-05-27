def concatenar(lista: list, lista2: list) -> list:
    lista3 = []
    lista3 = lista + lista2
    return lista3

lista = []
lista2 = []

can = int(input("Ingrese la cantiad de elementos que va a tener la primer lista: "))

for i in range(can):

    elementos = input("Ingrese el elemento " + str(i+1) + " de la primer lista: ")
    lista.append(elementos)

can2 = int(input("Ingrese la cantidad de elementos que va a tener la segunda lista: "))

for i in range(can2):

    elementos2 = input("Ingrese el elemento " + str((i+1)) + " de la segunda lista: ")
    lista2.append(elementos2)

lista3 = concatenar(lista, lista2)
print("Esta es la concatenación de las 2 listas: " + str(lista3))