################################
#Grupo Talavera y Fioroni
################################
n = int(input("Ingrese un número: "))

if n < 0:
    print ("El número debe ser positivo")
else:
    if n % 2 == 0:
        print (f"{n} es par")
    else:
        print (f"{n} es impar")