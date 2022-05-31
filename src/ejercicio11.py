z = int(input("Número: "))
conteo = 1
while z<500:
    conteo += 1
    z1=int(input("Número: "))
    if z1<0:
        z1 = abs(z1)
        print (f"{z} - {z1} = {z-z1}")
        z -= z1
    else:
        print (f"{z} + {z1} = {z+z1}")
        z+= z1
print (f" La suma de {conteo} numeros ingresados es: {z}")