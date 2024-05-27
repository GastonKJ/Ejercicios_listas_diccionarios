def invertir(lista: list) -> list:
    lista_inv = lista[::-1]
    return lista_inv

lista = []
can = int(input("Ingrese la cantidad de datos que quiera meter a la lista: "))

for i in range(can):
    elementos = input("Ingrese el elemento " + str(i+1) + " de la lista: ")
    lista.append(elementos)

lista_inv = invertir(lista)
print("Esta es la lista invertida: " + str(lista_inv))