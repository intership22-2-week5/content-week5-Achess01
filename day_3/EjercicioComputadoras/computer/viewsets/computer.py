""" Computer view """

# Django
from django.forms import ValidationError

# Rest framework
from rest_framework import viewsets, views, filters

# Filtering
from django_filters.rest_framework import DjangoFilterBackend

# Models
from ..models.computer import Computadora

# Serializer
from ..serializers.computer import ComputadoraSerializer

class ComputadoraViewSet(viewsets.ModelViewSet):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['nombre']
    ordering_fields = ['fecha_creacion', 'costo', 'cantidad']
    search_fields = ['$nombre']
    


    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
            return views.Response({"message": "Computer created successfully", "status": True})
        except ValidationError as ve:
            return views.Response({"message": ve.message, "status": False})