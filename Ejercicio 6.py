## Realiza un programa que permita generar un intervalo de los cubos
## de los primeros n números.
## Ejemplo: 1 + 8 + 27 + n 

def intesuma(x):
        a=[(conta**3) for conta in range(1,x+1)]
        print a
        return sum(a)
