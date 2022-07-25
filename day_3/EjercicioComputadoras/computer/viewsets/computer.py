""" Computer view """

# Django
from django.forms import ValidationError

# Rest framework
from rest_framework import viewsets, views

# Models
from ..models.computer import Computadora

# Serializer
from ..serializers.computer import ComputadoraSerializer

class ComputadoraViewSet(viewsets.ModelViewSet):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer

    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
            return views.Response({"message": "Computer created successfully", "status": True})
        except ValidationError as ve:
            return views.Response({"message": ve.message, "status": False})