################################
#Grupo Talavera y Fioroni
################################
x = float(input("Ingrese un número: "))
if x<-1 or x>1:
    print ("No pertenece a ningun intervalo")
else:
    if x >= -1 and x < 0:
        print ("Pertenece al intervalo [-1;0)")
    else:
        print ("Pertenece al intervalo (0;1]")
