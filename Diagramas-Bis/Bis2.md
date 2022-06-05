```python

l=[]
for i in range(8, 40):
    numeros=int(input("Ingrese número: "))
    l.append(numeros)
print (l)
limite = len(l)
for i in range(limite):
    if l[i] < 0:
        negativo = l[i]
    else:
        pass
print (f"El ultimo valor negativo es: {negativo}")

```
