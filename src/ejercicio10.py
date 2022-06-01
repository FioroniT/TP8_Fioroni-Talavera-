b = int(input("Ingrese un valor: "))
if b <= 0:
    print ("éste primer valor no puede ser negativo o igual a 0")
else:
    conteo = 1
    seguir = 1
    while seguir == 1:
        b = int(input("Ingrese un valor: "))
        if b == 0:
            print ("El valor ingresado no puede ser 0")
        else:
            if b<0:
                seguir = 0
                print (f"Cantidad de números ingresados: {conteo}")
            else:
                conteo +=1
