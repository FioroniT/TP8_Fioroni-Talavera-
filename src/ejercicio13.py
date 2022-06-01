p = int(input("Ingrese el multiplicando: "))
q = int(input("Ingrese el multiplicador: "))
contador = q

if p<0 or q<0:
    print ("Uno o ambos valores son negativos")
else:
    while contador>0:
        resultado = p + q
        print (f"{p} + {q} = {resultado}")
        p = resultado
        contador -=1