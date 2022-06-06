numero = int(input("Ingrese un numero entre 999 y 99999 :"))

if numero < 999 or numero > 99999:
    print ("Número fuera de rango")
else:
    print (f"El numero ingresado es: {numero}")
    num_str = str(numero)
    long_numero = len(num_str)
    if long_numero == 5:
        decena_mil = num_str[0]
        unidad_mil = num_str[1]
        centena = num_str [2]
        decena = num_str [3]
        unidad = num_str [4]
        if decena_mil == unidad and unidad_mil == decena:
            print (f"{numero} es capicúa")
        else:
            print (f"{numero} no es capicúa")
    elif long_numero ==4:
        unidad_mil = num_str[0]
        centena = num_str [1]
        decena = num_str [2]
        unidad = num_str [3]
        if unidad_mil == unidad and centena == decena:
            print (f"{numero} es capicúa")
        else:
            print (f"{numero} no es capicúa")
    else:
        centena = num_str [0]
        decena = num_str [1]
        unidad = num_str [2]
        if unidad == centena:
            print (f"{numero} es capicúa")
        else:
            print (f"{numero} no es capicúa")
            