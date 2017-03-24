## Realiza un programa que permita generar un intervalo de los cubos
## de los primeros n números.
## Ejemplo: 1 + 8 + 27 + n 

print("Suma de cubos de los primeros n numeros")
x = int(input("Ingrese un numero: "))
a=[(conta**3) for conta in range(1,x+1)]
suma = sum(a)
print("La suma de los cubos es: "+str(suma))
