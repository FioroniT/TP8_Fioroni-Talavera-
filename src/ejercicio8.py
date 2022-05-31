contador = 0
while contador < 6:
    n1 = int(input("Ingrese primera nota: "))
    if n1 <0:
        print ("La nota no puede ser menor a 0")
    else:
        n2 = int(input("Ingrese segunda nota: "))
        if n2<0:
            print ("Las notas no pueden ser negativas")
        else:
            resultado = (n1 + n2) / 2
            print (f"Promedio: {resultado}")
            contador +=1