numero = int(input("Introduce tu nota "))

if numero < 5:
    print("Suspenso")
elif numero >= 5 and numero <7:
    print("aprobado")
elif numero >=7 and numero < 9:
    print("Notable")
elif numero >= 9:
    print ("Sobresaliente")