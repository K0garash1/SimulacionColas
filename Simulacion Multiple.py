from utilidades import *
from sistema import *

l = 10
u = 15
s = 1.2
n= 10000

for i in range(20):
    print(f"-------Simulacion {i+1}-------")
    tasa_llegada = obtenerDistibucionPoisson(l, n)
    testPoisson(tasa_llegada, l)
    print(f"El promedio de la tasa de llegada es: {promedio(tasa_llegada)}")
    tasa_servicio = obtenerDistibucionNormal(u, s, n)
    testNorm(tasa_servicio, u, s)
    print(f"El promedio de la tasa de llegada es: {promedio(tasa_servicio)}")

    tiempos_llegadas = list(tasa_llegada.tolist())
    for i in range(0, len(tiempos_llegadas)):
        if tiempos_llegadas[i] == 0:
            tiempos_llegadas[i]=1
        #(minutos*100)/cliente
        tiempos_llegadas[i] = int(6000/tiempos_llegadas[i])
    
    tiempos_servicio = list(tasa_servicio.tolist())
    for i in range(0, len(tiempos_servicio)):
        #(minutos*100)/cliente
        tiempos_servicio[i] = int(6000/tiempos_servicio[i])
    
    #Simula el servicio
    serv = Servicio().Simular(acumular(tiempos_llegadas), tiempos_servicio)
    print(f"Se han simulado {len(serv.clientes_atendidos)}")
    print(f"Promedio de clientes en sistema: {promedio(serv.clientes_en_sistema)}")
    print(f"Promedio de clientes en cola: {promedio(serv.clientes_en_cola)}")
    tiempos_en_sistema = []
    for cliente in serv.clientes_atendidos:
        tiempo = cliente.tiempo_salida-cliente.tiempo_llegada
        tiempos_en_sistema.append(tiempo/100)
    print(f"El promedio de tiempo en sistema es: {promedio(tiempos_en_sistema)} minutos")
    tiempos_en_cola = []
    for cliente in serv.clientes_atendidos:
        tiempo = cliente.tiempo_atencion-cliente.tiempo_llegada
        tiempos_en_cola.append(tiempo/100)
    print(f"El promedio de tiempo en cola es: {promedio(tiempos_en_cola)} minutos")
    print("---------------------\n")