from django.db import models
from .models import Dispositivo

class Medicion(models.Model):
    """
    Modelo que representa una medición de consumo energético realizada por un dispositivo.
    """
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name='mediciones')  
    # Relación con el dispositivo que realizó la medición

    fecha_hora = models.DateTimeField(auto_now_add=True)  
    # Fecha y hora de la medición (se establece automáticamente al crear el objeto)

    valor = models.DecimalField(max_digits=10, decimal_places=2)  
    # Valor de la medición (puede ser consumo en kWh, temperatura, etc.)

    unidad = models.CharField(max_length=10, choices=[
        ('kWh', 'Kilovatio-hora'),
        ('°C', 'Grados Celsius'),
        ('estado', 'Estado (Encendido/Apagado)'),
        # Agrega más opciones según los tipos de medición que necesites
    ])  
    # Unidad de medida del valor

    def __str__(self):
        """
        Representación en cadena de la medición.
        """
        return f"Medición de {self.dispositivo} ({self.fecha_hora}): {self.valor} {self.unidad}"
