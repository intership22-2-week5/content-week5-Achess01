from turtle import up
from django.forms import ValidationError
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

    def validate(self, attrs):
        attrs = super().validate(attrs)
        ids = self.context['request'].data.getlist('computadoras')
        computadoras = Computadora.objects.filter(pk__in=ids)
        there_is_cantidad = True
        no_cantidad_message = "No stock: "
        total_price = 0
        """ Check for more than one of a same computer """
        for pc in computadoras:
            if pc.cantidad < 1:
                there_is_cantidad = False
                no_cantidad_message += f'{pc.__str__()} '

        if there_is_cantidad:
            for pc in computadoras:
                pc.cantidad -= 1
                pc.save(update=True)
                total_price += pc.costo

            attrs.update({"total": total_price})
        else:
            raise ValidationError(no_cantidad_message)

        return attrs

    class Meta:
        model = Orden
        fields = '__all__'
        read_only_fields = ['total']


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
