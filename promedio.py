def promedio(lista: list, elementos) -> float:
    suma = sum(lista)
    prom = suma / elementos
    return prom

lista = []
can = int(input("Ingrese la cantidad de datos que va a tener la lista: "))

for i in range(can):
    nro = float(input("Ingrese el dato número " + str(i+1) + " : "))
    lista.append(nro)
    
elementos = len(lista)
print("El promedio de los elementos de la lista es " + str(promedio(lista, elementos)))