def MaximoMinimo(numeros: list) -> float:
    return "El numero más grande es " + str(max(numeros)) + " y el más chico es "+  str(min(numeros))

numeros = []
can = int(input("Ingrese la cantidad de datos que desea tener en la lista: "))

for i in range(can):
    nro = float(input("Ingrese el número " + str(i+1) + " : "))
    numeros.append(nro)
print(MaximoMinimo(numeros))