""" Order view """

# Django
from django.forms import ValidationError

# Rest framework
from rest_framework import viewsets, views

# Models
from ..models.order import Orden

# Serializer

from ..serializers.order import OrdenSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def create(self, request, *args, **kwargs):
        try:
            # print(request.data)
            return super().create(request, *args, **kwargs)
        except ValidationError as ve:
            return views.Response({"message": ve.message, "status": False})