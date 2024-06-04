from django.db import models
from .models import Hogar

class Dispositivo(models.Model):
    """
    Modelo que representa un dispositivo (medidor inteligente o IoT) asociado a un hogar.
    """
    hogar = models.ForeignKey(Hogar, on_delete=models.CASCADE, related_name='dispositivos')  
    # Relación con el hogar al que pertenece el dispositivo

    nombre = models.CharField(max_length=100)  
    # Nombre descriptivo del dispositivo (ej: "Medidor Salón", "Termostato Habitación")

    tipo = models.CharField(max_length=50, choices=[
        ('medidor_energia', 'Medidor de Energía'),
        ('termostato', 'Termostato'),
        ('enchufe_inteligente', 'Enchufe Inteligente'),
        ('sensor_movimiento', 'Sensor de Movimiento'),
        ('otro', 'Otro'),
    ])  
    # Tipo de dispositivo (medidor, termostato, etc.)

    marca = models.CharField(max_length=50)
    # Marca del dispositivo

    modelo = models.CharField(max_length=50)
    # Modelo del dispositivo

    ubicacion = models.CharField(max_length=100, blank=True)  
    # Ubicación del dispositivo dentro del hogar (opcional)

    fecha_instalacion = models.DateField(null=True, blank=True)  
    # Fecha de instalación del dispositivo (opcional)

    def __str__(self):
        """
        Representación en cadena del dispositivo.
        """
        return f"{self.nombre} ({self.tipo}) en {self.hogar}"
