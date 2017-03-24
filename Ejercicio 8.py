## Realiza un programa que permita generar un
## intervalo de n numeros entre 20 y 60

print("intervalo de n numeros entre 20 y 60")
x = int(input("Ingrese el numero de intervalo: "))
cont=1
while cont<=x:
        if cont>=20 and cont<=60:
                cont+=1
print("El intervalo es"+str(cont))
