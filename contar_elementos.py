def contarElementos(lista: list, valor) -> int:
    con = 0
    for i in lista:
        if i == valor:
            con += 1
    return con

lista = []
can = int(input("Ingrese la cantidad de elementos de su lista: "))
for i in range(can):
    elementos = input("Ingrese el elemento " + str(i+1)+ " de su lista: ")
    lista.append(elementos)

valor = input("Ingrese un valor para saber cuantas veces aparece en la lista: ")
con  = contarElementos(lista, valor)
print("El valor se repitió " + str(con) + " veces en la lista")