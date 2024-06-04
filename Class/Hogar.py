from django.db import models
from .models import Usuario  # Importa el modelo Usuario creado anteriormente

class Hogar(models.Model):
    """
    Modelo que representa un hogar en el sistema.
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='hogares')  
    # Relación con el usuario propietario del hogar (un usuario puede tener varios hogares)

    nombre = models.CharField(max_length=100)  
    # Nombre descriptivo del hogar (ej: "Casa de Verano", "Apartamento Principal")

    direccion = models.CharField(max_length=255)
    # Dirección completa del hogar

    numero_habitantes = models.PositiveIntegerField(default=1)  
    # Número de personas que viven en el hogar

    tipo_vivienda = models.CharField(max_length=50, choices=[
        ('apartamento', 'Apartamento'),
        ('casa', 'Casa'),
        ('otro', 'Otro'),
    ], default='apartamento')  
    # Tipo de vivienda (apartamento, casa, otro)

    metros_cuadrados = models.PositiveIntegerField(null=True, blank=True)  
    # Tamaño del hogar en metros cuadrados (opcional)

    def __str__(self):
        """
        Representación en cadena del hogar.
        """
        return f"{self.nombre} ({self.direccion})"
