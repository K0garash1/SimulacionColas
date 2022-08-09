#Brayan Steven Arellano Espinosa - 20191020151

#Tasa de llegada promedio
l = None
while (True):
    print("Ingrese el parametro λ")
    while (True):
        try:
            l = float(input())
            break
        except:
            print("Ingrese un valor valido")
    print(f"El parametro λ ingresado es {l}, es correcto?\n (s/n)")
    if input()=="s":
        break
#Tasa de servicio promedio
u = None
while (True):
    print("Ingrese el parametro μ")
    while (True):
        try:
            u = float(input())
            break
        except:
            print("Ingrese un valor valido")
    print(f"El parametro μ ingresado es {u}, es correcto?\n (s/n)")
    if input()=="s":
        break
#Desviacion estandar
s = None
while (True):
    print("Ingrese la desviacion estandar σ")
    while (True):
        try:
            s = float(input())
            break
        except:
            print("Ingrese un valor valido")
    print(f"La desviacion estandar σ ingresada es {s}, es correcto?\n (s/n)")
    if input()=="s":
        break