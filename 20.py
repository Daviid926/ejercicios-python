import math
def factorial(n):
    cont = 1
    factor = 1
    while cont <= n:
        factor = factor*cont
        cont = cont +1
    return factor

numero = int(input("Introduce numero: "))
print(f"El factorial es {factorial(numero)}")