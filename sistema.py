class Servicio:
  clientes_en_sistema = []
  clientes_en_cola = []
  tiempo_transcurrido = 0
  #Lista de clientes que salen del sistema
  clientes_atendidos = []
  #Clientes en cola
  cola = []
  #Cliente en servidor
  actual = None

  def hayCola(self):
      return len(self.cola)>0
  
  #Simula un sistema de colas PEPS
  def Simular(self, momentos_llegadas, tiempos_servicio):
    n = len(momentos_llegadas)
    #Inicia simulacion hasta que sean atendidos todos los clientes
    t=0
    while len(self.clientes_atendidos)<n:
      #Salida del cliente actual
      if self.actual is not None:
        if t==self.actual.tiempo_salida:
          self.clientes_atendidos.append(self.actual)
          self.actual = None
      #Llega un nuevo cliente
      if len(momentos_llegadas)>0:
        if t == momentos_llegadas[0]:
          cliente = Cliente(momentos_llegadas[0], tiempos_servicio[0])
          momentos_llegadas.pop(0)
          tiempos_servicio.pop(0)
          self.cola.append(cliente)
      #Mueve el primer cliente en cola a servidor si esta libre
      if self.hayCola() & (self.actual is None):
        self.actual = self.cola.pop(0)
        self.actual.tiempo_salida=t+self.actual.tiempo_servicio
        self.actual.tiempo_atencion=t
      t+=1
      #Estadisticas
      self.tiempo_transcurrido = t
      self.clientes_en_cola.append(len(self.cola))
      if self.actual is not None:
        self.clientes_en_sistema.append(len(self.cola)+1)
      else:
        self.clientes_en_cola.append(len(self.cola))
    return self





class Cliente:
  #Tiempo de llegada: instante de tiempo en el que el cliente ingresa al sistema
  tiempo_llegada = 0
  #Tiempo de atencion: instante de tiempo en el que el cliente es movido de cola a servidor
  tiempo_atencion = 0
  #Tiempo de servicio: unidades de tiempo que el cliente tarda en servidor
  tiempo_servicio = 0
  #Tiempo de salida: instante de tienpo en el que el cliente sale del sistema
  tiempo_salida = 0
  #Nuevo cliente
  def __init__(self, t_ll, t_s):
    self.tiempo_llegada = t_ll
    self.tiempo_servicio = t_s