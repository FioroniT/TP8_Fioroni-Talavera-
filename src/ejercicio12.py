contador = 0
negativo = 0
positivo = 0
cero = 0

while contador < 10:
    x = int(input("Número: "))
    if x == 0:
        cero += 1
        contador +=1
    else:
        if x > 0:
            positivo +=1
            contador +=1
        else:
            negativo +=1
            contador +=1
print (f" Positivos: {positivo}\n Negativos: {negativo}\n Ceros: {cero}")