import random
from random import *

l=[]
for i in range(20):
    numeros=randrange(-5, 5)
    l.append(numeros)
positivo = 0
negativo = 0
cero = 0
limite = len(l)
for i in range(limite):
    if l[i]== 0:
        cero +=1
    else:
        if l[i] < 1:
            positivo += 1
        else:
            negativo += 1
    print (f"Positivos: {positivo}\nNegativos: {negativo}\nCeros: {cero}")