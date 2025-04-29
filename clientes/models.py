from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):

    razon_social = models.CharField(max_length=255, verbose_name="Razón Social", blank=True, null=True)
    cif = models.CharField(max_length=20, unique=True, verbose_name="CIF/NIF")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
