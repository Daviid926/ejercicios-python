lista = []
contador = 0
sum = 0
while contador < 5:
    numero = float(input("Introduce numero: "))
    lista.append(numero)
    contador = contador+1
    sum = sum+numero
media = sum / 5
print (f"La media es {media}")
