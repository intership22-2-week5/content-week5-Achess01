from rest_framework import serializers

from .models import Raton, Teclado, Monitor, Orden, Computadora, PlacaBase, CPU, Altavoz


class RatonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raton
        fields = '__all__'


class TecladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teclado
        fields = '__all__'


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'


class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__'


class ComputadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computadora
        exclude = ('fecha_creacion',)
        read_only_fields = ['costo']


class PlacaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacaBase
        fields = '__all__'


class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'


class AltavozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Altavoz
        fields = '__all__'
