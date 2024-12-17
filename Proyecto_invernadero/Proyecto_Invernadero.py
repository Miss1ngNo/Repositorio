class SensorTemperatura:
    def __init__(self, temperatura_actual, temperatura_objetivo):
        self.temperatura_actual = temperatura_actual
        self.temperatura_objetivo = temperatura_objetivo

    def ajustar_temperatura(self):
        if self.temperatura_actual < self.temperatura_objetivo:
            self.temperatura_actual = self.temperatura_objetivo
        elif self.temperatura_actual > self.temperatura_objetivo:
            self.temperatura_actual = self.temperatura_objetivo

                
class SensorHumedad:
    def __init__(self, humedad_actual, humedad_objetivo):
        self.humedad_actual = humedad_actual
        self.humedad_objetivo = humedad_objetivo

    def ajustar_humedad(self):
        if self.humedad_actual < self.humedad_objetivo:
            self.humedad_actual = self.humedad_objetivo
        elif self.humedad_actual > self.humedad_objetivo:
            self.humedad_actual = self.humedad_objetivo
                
class ActuadorLuz:
    def __init__(self, luz_actual, luz_objetivo, luminosidad):
        self.luz_actual = luz_actual
        self.luz_objetivo = luz_objetivo
        self.luminosidad = luminosidad

    def ajustar_luz(self):
        if self.luz_actual < self.luz_objetivo:
            self.luminosidad += 1 
            if self.luz_actual > self.luz_objetivo:
                self.luz_actual = self.luz_objetivo
        elif self.luz_actual > self.luz_objetivo:
            self.luminosidad -= 1
            if self.luz_actual < self.luz_objetivo:
                self.luz_actual = self.luz_objetivo

class ControladorInvernadero:
    def __init__(self):
        self.sensor_temperatura = SensorTemperatura(20, 20) #Grados C, Grados C, Estado True o False
        self.sensor_humedad = SensorHumedad(60, 60) #%Humedad,%Humedad, Estado True o False
        self.actuador_luz = ActuadorLuz(12000, 12000, 50)  #Luxes, Luxes, %Iluminosidad
        
    def ajustar_variables(self, temperatura, humedad, luz):
       self.sensor_temperatura.temperatura_objetivo = temperatura
       self.sensor_humedad.humedad_objetivo = humedad
       self.actuador_luz.luz_objetivo = luz
       
       #Actualiza las variables
       self.sensor_temperatura.ajustar_temperatura()
       self.sensor_humedad.ajustar_humedad()
       self.actuador_luz.ajustar_luz()

    def obtener_variables(self):
        return {
            "temperatura": self.sensor_temperatura.temperatura_actual,
            "humedad": self.sensor_humedad.humedad_actual,
            "luz": self.actuador_luz.luz_actual
        }

#Ejemplo de uso
controlador = ControladorInvernadero()
controlador.ajustar_variables(25, 65, 15000)

