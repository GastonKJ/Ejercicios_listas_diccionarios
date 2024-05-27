def NoDuplicados(lista: list) -> set:
    listaLimpia = set(lista)
    return listaLimpia

lista = []
can = int(input("Ingrese la cantidad de elementos de su lista: "))

for i in range(can):
   
   elemento = input("Ingrese el elemento " + str(i+1) + " de la lista: ")
   lista.append(elemento)
   
listaLimpia = NoDuplicados(lista)
print("Esta es la lista sin duplicados: " + str(listaLimpia) )