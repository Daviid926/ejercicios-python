cadena = str(input("Introduce frase "))
cadena = cadena.lower() 
long = len(cadena)-1
contador = 0
while long >=0:
    if cadena[long] =="a" or cadena[long] =="e" or cadena[long] =="i" or cadena[long] =="o" or cadena[long] =="u" :
        contador = contador+1
    long = long-1   
print (f"El numero de vocales es {contador}")



