""" Computer Serializer """

# Django rest framework
from rest_framework import serializers

# Computer model
from ..models.computer import Computadora

class ComputadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computadora
        exclude = ('fecha_creacion',)
        read_only_fields = ['costo']