def producto(lista: list[float]) -> float:
    pro = 1
    for nro in lista:
        pro *= nro
    return pro

lista = []
can = int(input("Ingrese la cantidad de número que va a tener su lista: "))

for i in range(can):

    nro = float(input("Ingrese el número " + str(i+1) + " de la lista: "))
    lista.append(nro)
pro = producto(lista)
print("El producto de los elementos de la lista es " + str(pro))