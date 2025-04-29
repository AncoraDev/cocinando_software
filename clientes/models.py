from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    razon_social = models.CharField(max_length=255, verbose_name="Razón Social", blank=True, null=True)
    cif = models.CharField(max_length=20, unique=True, verbose_name="CIF/NIF")

    email = models.EmailField(max_length=255, verbose_name="Email", blank=True, null=True)
    password = models.CharField(max_length=255, verbose_name="Contraseña", blank=True, null=True)

    def __str__(self):
        return self.nombre
