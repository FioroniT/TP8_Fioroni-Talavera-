``` mermaid

import random
from random import *

def signo(l):
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
    return positivo, negativo, cero 

def principal():
    l=[]
    for i in range(20):
        numeros=randrange(-5, 5)
        l.append(numeros)
    print (signo(l))
if __name__=="__main__":
    principal()
```
