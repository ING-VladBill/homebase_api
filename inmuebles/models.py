from django.db import models


class Propietario(models.Model):
    """Representa a la persona propietaria de uno o más inmuebles."""

    nombre = models.CharField(max_length=120)
    documento_identidad = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Propietario"
        verbose_name_plural = "Propietarios"

    def __str__(self):
        return f"{self.nombre} - {self.documento_identidad}"


class Propiedad(models.Model):
    """Representa una propiedad inmobiliaria asociada a un propietario."""

    class TipoPropiedad(models.TextChoices):
        CASA = "casa", "Casa"
        DEPARTAMENTO = "departamento", "Departamento"
        TERRENO = "terreno", "Terreno"
        LOCAL = "local", "Local comercial"
        OFICINA = "oficina", "Oficina"
        OTRO = "otro", "Otro"

    direccion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    tipo = models.CharField(
        max_length=30,
        choices=TipoPropiedad.choices,
        default=TipoPropiedad.CASA,
    )
    descripcion = models.TextField(blank=True)
    propietario = models.ForeignKey(
        Propietario,
        related_name="propiedades",
        on_delete=models.CASCADE,
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["direccion"]
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"

    def __str__(self):
        return f"{self.direccion} ({self.get_tipo_display()})"
