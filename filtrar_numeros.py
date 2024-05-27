def filtro(lista: list, nron: float) -> list:
    lista2 = []
    for i in lista:
        if i > nron:
            lista2.append(i) 
    return lista2

lista= []
can = int(input("Ingrese el numero de elementos de su lista: "))
nron = float(input("Ingrese el valor minimo para generar la nueva lista: "))

for i in range(can):
    nro = float(input("Ingrese el numero " + str(i+1)+ " : "))
    lista.append(nro)

lista2 = filtro(lista, nron)
print("La nueva lista es " + str(lista2))