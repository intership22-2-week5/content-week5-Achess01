""" Components views """

# Rest framework
from rest_framework import viewsets

# Serializers
from ..serializers.components import MonitorSerializer, RatonSerializer, TecladoSerializer, PlacaBaseSerializer, CPUSerializer, AltavozSerializer

# Models
from ..models.components import Raton, Teclado, Monitor, PlacaBase, CPU, Altavoz

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