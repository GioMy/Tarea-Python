## Realice una función que permita rotar una lista.
## rota 1 [3,2,5,7] == [2,5,7,3]
## rota 2 [3,2,5,7] == [5,7,3,2]
## rota 3 [3,2,5,7] == [7,3,2,5]


lista = [3,2,5,7]
print("Rotar una lista");
cont=1
while cont<len(lista):
        lista.append(lista[0])
        lista.remove(lista[0])
        cont +=1
        print (lista)
