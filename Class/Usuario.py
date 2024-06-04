from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Administrador personalizado para el modelo de usuario
class UsuarioManager(BaseUserManager):
    def create_user(self, correo_electronico, nombre, direccion, contrasena=None):
        """
        Crea y guarda un usuario con el correo electrónico, nombre, dirección y contraseña proporcionados.
        """
        if not correo_electronico:
            raise ValueError('Los usuarios deben tener un correo electrónico')

        user = self.model(
            correo_electronico=self.normalize_email(correo_electronico),
            nombre=nombre,
            direccion=direccion,
        )

        user.set_password(contrasena)  # Encripta la contraseña antes de guardarla
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_electronico, nombre, direccion, contrasena):
        """
        Crea y guarda un superusuario con el correo electrónico, nombre, dirección y contraseña proporcionados.
        """
        user = self.create_user(
            correo_electronico,
            nombre=nombre,
            direccion=direccion,
            contrasena=contrasena,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Modelo de usuario personalizado
class Usuario(AbstractBaseUser):
    correo_electronico = models.EmailField(
        verbose_name='Correo Electrónico',
        max_length=255,
        unique=True,
    )
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # Indica si el usuario está activo
    is_admin = models.BooleanField(default=False)  # Indica si el usuario es administrador

    objects = UsuarioManager()  # Asigna el administrador personalizado al modelo

    USERNAME_FIELD = 'correo_electronico'  # Campo utilizado para la autenticación
    REQUIRED_FIELDS = ['nombre', 'direccion']  # Campos requeridos al crear un superusuario

    def __str__(self):
        return self.correo_electronico

    def has_perm(self, perm, obj=None):
        """
        Verifica si el usuario tiene un permiso específico.
        """
        return True

    def has_module_perms(self, app_label):
        """
        Verifica si el usuario tiene permisos para ver la aplicación.
        """
        return True

    @property
    def is_staff(self):
        """
        Indica si el usuario es miembro del personal.
        """
        return self.is_admin
