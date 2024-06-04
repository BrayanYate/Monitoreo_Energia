from django.db import models
from .models import Usuario

class Recomendacion(models.Model):
    """
    Modelo que representa una recomendación personalizada para un usuario.
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='recomendaciones')  
    # Relación con el usuario al que se dirige la recomendación

    fecha_creacion = models.DateTimeField(auto_now_add=True)  
    # Fecha y hora en que se creó la recomendación

    descripcion = models.TextField()  
    # Descripción detallada de la recomendación (qué hacer y por qué)

    tipo = models.CharField(max_length=50, choices=[
        ('ahorro_energia', 'Ahorro de Energía'),
        ('eficiencia_electrodomesticos', 'Eficiencia de Electrodomésticos'),
        ('climatizacion', 'Climatización'),
        ('iluminacion', 'Iluminación'),
        ('otros', 'Otros'),
    ], default='ahorro_energia')  
    # Tipo de recomendación (categoría)

    prioridad = models.CharField(max_length=20, choices=[
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ], default='media')  
    # Prioridad de la recomendación (alta, media, baja)

    potencial_ahorro = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  
    # Potencial de ahorro estimado en kWh o moneda local (opcional)

    def __str__(self):
        """
        Representación en cadena de la recomendación.
        """
        return f"Recomendación para {self.usuario}: {self.descripcion[:50]}..."  
        # Muestra los primeros 50 caracteres de la descripción
