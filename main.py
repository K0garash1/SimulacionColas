#Brayan Steven Arellano Espinosa - 20191020151

from utilidades import *
from sistema import *


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

print(f"Iniciando simulacion para {n} clientes")
#Tiempos entre llegada de cliente (en minutos)
llegada_clientes = list(distPoisson.tolist())
for i in range(0, len(llegada_clientes)):
    if llegada_clientes[i] == 0:
        llegada_clientes[i]=1
    #(minutos*100)/cliente
    llegada_clientes[i] = int(6000/llegada_clientes[i])
llegada_clientes = acumular(llegada_clientes)

#Duracion del cliente en servidor (Tiempo de servicio en minutos)
atencion_clientes = list(distNormal.tolist())
for i in range(0, len(atencion_clientes)):
    #(minutos*100)/cliente
    atencion_clientes[i] = int(6000/atencion_clientes[i])

#Lista de clientes que salen del sistema
clientes_atendidos = []

t=0
s = Servicio()

while len(clientes_atendidos)<n:
    #Salida del cliente actual
    if s.actual is not None:
        if t==s.actual.tiempo_salida:
            clientes_atendidos.append(s.actual)
            s.actual = None
    #Llega un nuevo cliente
    if len(llegada_clientes)>0:
        if t == llegada_clientes[0]:
            cliente = Cliente(llegada_clientes[0], atencion_clientes[0])
            llegada_clientes.pop(0)
            atencion_clientes.pop(0)
            s.cola.append(cliente)
    #Mueve el primer cliente en cola a servidor
    if s.hayCola() & (s.actual is None):
        s.actual = s.cola.pop(0)
        s.actual.tiempo_salida=t+s.actual.tiempo_servicio
        s.actual.tiempo_atencion=t
    t+=1

#Total clientes atendidos
print(f"Total de clientes atendidos: {len(clientes_atendidos)}")

#Tiempos promedio en sistema y en cola
ws = 0
wq = 0

for i in range(0, len(clientes_atendidos)):
    #Tiempo en sistema = Tiempo de salida - Tiempo de llegada
    ws+=clientes_atendidos[i].tiempo_salida - clientes_atendidos[i].tiempo_llegada
    #Tiempo en cola = Tiempo de atencion- tiempo de llegada
    wq+= clientes_atendidos[i].tiempo_atencion - clientes_atendidos[i].tiempo_llegada

#Suma de tiempos/Total de clientes
ws/=len(clientes_atendidos)
wq/=len(clientes_atendidos)

print(f"Tiempo en sistema: {ws/100} minutos")
print(f"Tiempo en cola: {wq/100} minutos")