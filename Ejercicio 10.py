##Crear un programa que por medio de recursión calcule
##la suma de los cuadrados de n números.

def recursividad (dato, var=0):
        if(dato>=0):
                var+=dato**2
                return recursividad-1,var
        else:
                print var
