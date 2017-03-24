##Crear un programa que por medio de recursión calcule
##la suma de los cuadrados de n números.

print("Recursividad")
dato = input("ingrese un numero:")
variable=0
if(dato>=0):
    variable+=dato**2
    return recu(dato-1,variable)
        else:
     print variable

print("El Resultado es:"+str(variable))
