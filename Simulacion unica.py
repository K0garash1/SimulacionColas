#Brayan Steven Arellano Espinosa - 20191020151

from utilidades import *
from sistema import *


#OBTENCION DE PARAMETROS
#Tasa de llegada promedio
l = None
while (True):
    print("Ingrese la tasa de llegada promedio λ (Clientes/Hora)")
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
    print("Ingrese la tasa de servicio promedio μ (Clientes/Hora)")
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
graficarDistribucion(distPoisson, "Distribucion Poisson generada", l, 0)
distNormal = obtenerDistibucionNormal(u, s, n)
graficarDistribucion(distNormal, "Distribucion Normal generada", u, s)


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

#Duracion del cliente en servidor (Tiempo de servicio en minutos)
atencion_clientes = list(distNormal.tolist())
for i in range(0, len(atencion_clientes)):
    #(minutos*100)/cliente
    atencion_clientes[i] = int(6000/atencion_clientes[i])

#Simula el servicio
s = Servicio().Simular(acumular(llegada_clientes), atencion_clientes)
print(f"Se han simulado {len(s.clientes_atendidos)}")
print(f"Promedio de clientes en sistema: {promedio(s.clientes_en_sistema)}")
graficarLista(s.clientes_en_sistema, "Clientes en sistema")
print(f"Promedio de clientes en cola: {promedio(s.clientes_en_cola)}")
graficarLista(s.clientes_en_cola, "Clientes en cola")
tiempos_en_sistema = []
for cliente in s.clientes_atendidos:
    tiempo = cliente.tiempo_salida-cliente.tiempo_llegada
    tiempos_en_sistema.append(tiempo/100)
print(f"El promedio de tiempo en sistema es: {promedio(tiempos_en_sistema)} minutos")
graficarLista(tiempos_en_sistema, "Tiempos en sistema")
tiempos_en_cola = []
for cliente in s.clientes_atendidos:
    tiempo = cliente.tiempo_atencion-cliente.tiempo_llegada
    tiempos_en_cola.append(tiempo/100)
print(f"El promedio de tiempo en cola es: {promedio(tiempos_en_cola)} minutos")
graficarLista(tiempos_en_cola, "Tiempos en cola")