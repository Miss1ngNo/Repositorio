from django.db import models

class Variables(models.Model):
    temperatura = models.FloatField()
    humedad = models.FloatField()
    luz = models.FloatField()

    def __str__(self):
        return f"ID {self.id}: Temp={self.temperatura}, Hum={self.humedad}, Luz={self.luz}"
