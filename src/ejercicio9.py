a = int(input("Ingrese un número: "))
if a <0:
    print (f" El número ingresado no puede ser menor a 0!")
else:
    if a % 3 == 0:
        print (f" {a} es múltiplo de 3")
    else:
        print (f" {a} no es múltiplo de 3")