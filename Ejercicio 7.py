##Realiza un programa que permita generar un intervalo de los
## cuadrados de n números mayores a 100.

def sumMayor(x):
        vacio=[(conta**2) for conta in range(1,x+1)]        
        num=1
        while num<len(vacio):
                if vacio[num]>100:
                        print vacio[num]
                num+=1
