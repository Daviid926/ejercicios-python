cadena = str(input("Introduce palabra "))
numero = len(cadena) -1
reves = ""
while numero >=0:
    reves = (reves+cadena[numero])
    numero = numero -1
print (reves)