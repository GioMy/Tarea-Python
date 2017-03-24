import math
##Realiza un programa que solicite dos argumentos de tipo Double para
## calcular la hipotenusa de un triángulo rectángulo y
## retorne un valor de tipo Double.

print("Hiponetusa de un triangulo rectangulo")
b = float(input("Ingrese valor de b: "))
c = float(input("Ingresa valor de c: "))
Hipotenusa = float(math.sqrt(b**2 + c**2))
print("La Hiponetusa es: "+str(Hipotenusa))
