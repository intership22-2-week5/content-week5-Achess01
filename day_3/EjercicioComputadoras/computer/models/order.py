""" Order model class """

# Django
from django.db import models

# Models
from .computer import Computadora


class Orden(models.Model):
    description = models.CharField(max_length=255, default="Orden")
    computadoras = models.ManyToManyField(Computadora)
    total = models.FloatField(default=0)

    def __str__(self) -> str:
        return f'{self.description}'
