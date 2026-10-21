lista = []
contador = 0
while contador < 5:
    numero = float(input("Introduce numero: "))
    lista.append(numero)
    contador = contador+1

sin_repetidos = []

for elemento in lista:
    if elemento not in sin_repetidos:
        sin_repetidos.append(elemento)
print(sin_repetidos)