# Punto A y B
a = 0
lista=[]
while a <10:
    elementos = int(input("Ingrese un número entre -15 y 50: "))
    lista.append(elementos)
    if elementos < -15 or elementos > 50:
        print ("Número fuera de rango establecido.\nPor favor, ingrese nuevamente")
    else:
        a += 1
        
#Punto C

limite = len(lista)
c = 0
for i in range(limite):
    a = lista[i]
    c = c + a
print (f" suma {c}")

#Punto D

limite = len(lista)
d = 0
for i in range(limite):
    if i % 2 == 0:
        pass
    else:
        a = lista[i]
        d = d + a
print (f"posiciones impares {d}")

#Punto E

limite = len(lista)
e = 0
for i in range(limite):
    a = lista[i]
    e = e + a

promedio = e / limite
print (f"promedio es: {promedio}")

#Punto F
limite = len(lista)
f = 0
for i in range(limite):
    if lista[i] < 0:
        f += 1
porcentaje = (f * 100) / 10
print (f" porcentaje es: {porcentaje}")