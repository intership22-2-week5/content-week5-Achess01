from django.forms import ValidationError
from django.shortcuts import render

from rest_framework import viewsets, views

from .serializers import ComputadoraSerializer, MonitorSerializer, OrdenSerializer, RatonSerializer, TecladoSerializer, PlacaBaseSerializer, CPUSerializer, AltavozSerializer
from .models import Raton, Teclado, Monitor, Orden, Computadora, PlacaBase, CPU, Altavoz


class RatonViewSet(viewsets.ModelViewSet):
    queryset = Raton.objects.all()
    serializer_class = RatonSerializer


class TecladoViewSet(viewsets.ModelViewSet):
    queryset = Teclado.objects.all()
    serializer_class = TecladoSerializer


class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer


class PlacaBaseViewSet(viewsets.ModelViewSet):
    queryset = PlacaBase.objects.all()
    serializer_class = PlacaBaseSerializer


class CPUViewSet(viewsets.ModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer


class AltavozViewSet(viewsets.ModelViewSet):
    queryset = Altavoz.objects.all()
    serializer_class = AltavozSerializer


class OrdenViewSet(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as ve:
            return views.Response({"message": ve.message, "stock": False})


class ComputadoraViewSet(viewsets.ModelViewSet):
    queryset = Computadora.objects.all()
    serializer_class = ComputadoraSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as ve:
            return views.Response({"message": ve.message, "stock": False})
