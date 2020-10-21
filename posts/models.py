from django.utils import timezone as tz
from django.db import models


class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField("Título", max_length=200)
    text = models.TextField("Contenido")

    created_date = models.DateTimeField("Fecha de creación", default=tz.now)
    published_date = models.DateTimeField("Fecha de publicación", blank=True, null=True)

    def publish(self):
        self.published_date = tz.now()
        self.save()

    def __str__(self):
        return self.title


class Marca(models.Model):
    """La marca de un autmóvil representa...

    Puede ser de varias líneas

    """
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200)

    creacion = models.DateTimeField(default=tz.now)
    actualizacion = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.actualizacion = tz.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre}"


class Vehiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    referencia = models.CharField(max_length=20)
    nota = models.TextField()
    estaeliminado = models.BooleanField(default=False)

    creacion = models.DateTimeField(default=tz.now)
    actualizacion = models.DateTimeField(blank=True, null=True)

    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)

    def __str__(self):
        return f"Vehículo: {self.placa}"

    def save(self, *args, **kwargs):
        self.actualizacion = tz.now()
        return super().save(*args, **kwargs)
