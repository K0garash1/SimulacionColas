#Brayan Steven Arellano Espinosa - 20191020151

from utilidades import *

#OBTENCION DE PARAMETROS
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
    if input(f"El parametro λ ingresado es {l}, es correcto?\n(s/n) ")=="s":
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
    if input(f"El parametro μ ingresado es {u}, es correcto?\n(s/n) ")=="s":
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
    if input(f"La desviacion estandar σ ingresada es {s}, es correcto?\n(s/n) ")=="s":
        break
#Numero de clientes
n = None
while (True):
    print("Ingrese el numero de clientes a simular")
    while (True):
        try:
            n = int(input())
            break
        except:
            print("Ingrese un valor valido")
    if input(f"El valor ingresado es {n}, es correcto?\n(s/n) ")=="s":
        break

#GENERACION DE DATOS
distPoisson = obtenerDistibucionPoisson(l, n)
distNormal = obtenerDistibucionNormal(u, s, n)

#TEST DE DATOS
if input("Desea realizar un test de Kolmogorov–Smirnov para la distribucion de poisson generada?\n(s/n) ")=="s":
    testPoisson(distPoisson, l)
if input("Desea realizar un test de Kolmogorov–Smirnov para la distribucion normal generada?\n(s/n) ")=="s":
    testNorm(distNormal, u, s)

#SIMULACION