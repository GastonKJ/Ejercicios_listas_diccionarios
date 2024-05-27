def Indice(lista: list, valor) -> int:
    try:
        indice = lista.index(valor)
        return indice
    except ValueError:
        return -1
    
lista = []
can = int(input("Ingrese la cantidad de datos que quiera meter en la lista: "))
for i in range(can):
    elemento = input("Ingrese el elemento número " + str(i+1) + " de la lista: ")

valor = int(input("Ingrese un valor para buscar su índice en la lista: "))
indice = Indice(lista, valor)

if indice != -1:
    print(f"El índice del valor " + {valor} + " en la lista es:" + {indice})
else:
    print(f"El valor {valor} no se encuentra en la lista.")