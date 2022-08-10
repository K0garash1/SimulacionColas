class Servicio:
    cola = []
    actual = None
    def hayCola(self):
        return len(self.cola)>0


#Tiempo de llegada: instante de tiempo en el que el cliente ingresa al sistema
#Tiempo de atencion: instante de tiempo en el que el cliente es movido de cola a servidor
#Tiempo de servicio: unidades de tiempo que el cliente tarda en servidor
#Tiempo de salida: instante de tienpo en el que el cliente sale del sistema
class Cliente:
  tiempo_llegada =0
  tiempo_atencion = 0
  tiempo_servicio = 0
  tiempo_salida = 0
  def __init__(self, t_ll, t_s):
    self.tiempo_llegada = t_ll
    self.tiempo_servicio = t_s