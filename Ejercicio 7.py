##Realiza un programa que permita generar un intervalo de los
## cuadrados de n números mayores a 100.

print("Cuadrado de n numeros mayores a 100")
x = 13
v=[(conta**2) for conta in range(1,x+1)]
num = 1
while num<len(v):
        if v[num]>100:
                print (v[num])
                num+=1
print("El intervalo de los n numeros al Cuadrado son:"+str(v))
