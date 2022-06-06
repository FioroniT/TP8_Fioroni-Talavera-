lista=[]
for i in range(8, 40):
    numeros=int(input("Ingrese número: "))
    lista.append(numeros)
limite = len(lista)
for i in range(limite):
    if lista[i] < 0:
        negativo = lista[i]
        posicion = i + 1
    else:
        pass
if posicion == 0:
    print ("No se ingresaron valores negativos")
else:
    print (f"El último valor negativo es {negativo} y esta en la posicion: {posicion}")