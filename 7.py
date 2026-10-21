numero = int(input("Introduce un numero "))
numero2 = int(input("Introduce un numero "))
numero3 = int(input("Introduce un numero "))

if numero > numero2:
    if numero > numero3:
        print (f"El numero mayor es {numero}")      
    else:
        print (f"El numero mayor es {numero3}")
if numero2 > numero3:
    print (f"El numero mayor es el {numero2}")
else:
    print (f"El numero mayor es el {numero3}")