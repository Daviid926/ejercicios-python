lista = []
numero = float(input("Introduce numero: "))
lista.append(numero)
max = numero
min = numero
contador = 1
while contador < 5:
    numero = float(input("Introduce numero: "))
    lista.append(numero)
    if max < numero:
        max = numero
    if min > numero:
        min = numero 
    contador = contador+1
print (f"El numero mas alto es {max}")
print (f"El numero mas bajo es {min}")
