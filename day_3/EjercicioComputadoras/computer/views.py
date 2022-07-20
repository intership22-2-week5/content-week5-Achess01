from django.shortcuts import render

from rest_framework import viewsets, views

from .serializers import ComputadoraSerializer, MonitorSerializer, OrdenSerializer, RatonSerializer, TecladoSerializer
from .models import Raton, Teclado, Monitor, Orden, Computadora


class RatonViewSet(viewsets.ModelViewSet):
    queryset = Raton.objects.all()
    serializer_class = RatonSerializer


class TecladoViewSet(viewsets.ModelViewSet):
    queryset = Teclado.objects.all()
    serializer_class = TecladoSerializer


class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer


class ComputadoraViewSet(viewsets.ModelViewSet):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer

    def create(self, request, *args, **kwargs):
        pc = super().create(request, *args, **kwargs)        
        if pc.data['id'] is not None:
            return pc
        else:
            return views.Response({"message": "No hay stock"})
