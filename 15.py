cadena = str(input("Introduce palabra "))
cadena = cadena.lower()
long = len(cadena)-1
reves = ""
while long >= 0:
    reves = reves+cadena[long]
    long = long -1
if reves == cadena:
    print("La palabra es un palindromo")
else:
    print ("La palabra no es un palindromo")