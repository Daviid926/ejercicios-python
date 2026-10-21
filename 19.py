import math
def esPrimo(n):
    if n == 1:
        return True
    if n < 1 :
        return False
    if n == 2 :
        return True
    for i in range(3,n-1,2):
        if n%i == 0:
            return False
    return True

numero = int(input("Introduce un numero "))
if esPrimo(numero):
    print ("El numero es primo ")
else:
    print("El numero no es primo")


