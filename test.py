from utilidades import *
from sistema import *

n=5000
#Clientes/hora
l=10
#Clientes/hora
u=15
s=1.2

distPoisson = obtenerDistibucionPoisson(l, n)
distNormal = obtenerDistibucionNormal(u, s, n)

#SIMULACION
llegada_clientes = list(distPoisson.tolist())
for i in range(0, len(llegada_clientes)):
    if llegada_clientes[i] == 0:
        llegada_clientes[i]=1
    #(minutos*100)/cliente
    llegada_clientes[i] = int(6000/llegada_clientes[i])
llegada_clientes = acumular(llegada_clientes)

atencion_clientes = list(distNormal.tolist())
for i in range(0, len(atencion_clientes)):
    #(minutos*100)/cliente
    atencion_clientes[i] = int(6000/atencion_clientes[i])


clientes_atendidos = []

t=0
s = Servicio()

while len(clientes_atendidos)<n:
    #Salida del cliente actual
    if s.actual is not None:
        if t==s.actual.tiempo_salida:
            #print(f"[{t}] sale cliente de servidor")
            clientes_atendidos.append(s.actual)
            s.actual = None
    #Llega un nuevo cliente
    if len(llegada_clientes)>0:
        if t == llegada_clientes[0]:
            cliente = Cliente(llegada_clientes[0], atencion_clientes[0])
            llegada_clientes.pop(0)
            atencion_clientes.pop(0)
            s.cola.append(cliente)
            #print(f"[{t}] entra cliente al sistema")
    #Mueve el primer cliente en cola a servidor
    if s.hayCola() & (s.actual is None):
        s.actual = s.cola.pop(0)
        s.actual.tiempo_salida=t+s.actual.tiempo_servicio
        s.actual.tiempo_atencion=t
        #print(f"[{t}] entra cliente a servidor")
    t+=1

#Total clientes atendidos
print(len(clientes_atendidos))

ws = 0
wq = 0

for i in range(0, len(clientes_atendidos)):
    #Tiempo de salida - Tiempo de llegada
    ws+=clientes_atendidos[i].tiempo_salida - clientes_atendidos[i].tiempo_llegada
    #Tiempo de atencion- tiempo de llegada
    wq+= clientes_atendidos[i].tiempo_atencion - clientes_atendidos[i].tiempo_llegada

#Suma de tiempos/Total de clientes
ws/=len(clientes_atendidos)
wq/=len(clientes_atendidos)

print(f"Tiempo en sistema: {ws/100} minutos")
print(f"Tiempo en cola: {wq/100} minutos")