""" Order serializer """

# Django
from django.forms import ValidationError

# Rest framework
from rest_framework import serializers

# Models

from ..models.computer import Computadora
from ..models.order import Orden


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
