def suma_elementos(lista: list) -> float:
    return sum(lista)

can = int(input("Ingrese la cantidad de datos que quiere ingresar en la lista: "))
lista = []

for i in range(can):
    nro = float(input("Ingrese el dato número "+ str(i+1) + " : " ))
    lista.append(nro)
    suma = suma_elementos(lista)
print(suma)