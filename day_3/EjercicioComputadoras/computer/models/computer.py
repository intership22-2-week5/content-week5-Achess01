""" Components models """

# Django
from django.db import models
from django.forms import ValidationError

# Models
from .components import Monitor, Teclado, Altavoz, PlacaBase, CPU, Raton

class Computadora(models.Model):
    nombre = models.CharField(max_length=255)
    monitor = models.ForeignKey(
        Monitor, on_delete=models.SET_NULL, null=True)
    raton = models.ForeignKey(Raton, on_delete=models.SET_NULL, null=True)
    teclado = models.ForeignKey(
        Teclado, on_delete=models.SET_NULL, null=True)
    altavoz = models.ForeignKey(
        Altavoz, on_delete=models.SET_NULL, null=True)
    cpu = models.ForeignKey(
        CPU, on_delete=models.SET_NULL, null=True)
    placabase = models.ForeignKey(
        PlacaBase, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=1)
    costo = models.FloatField(default=0)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def get_components(self):
        monitor = Monitor.objects.filter(pk=self.monitor.id)
        raton = Raton.objects.filter(pk=self.raton.id)
        teclado = Teclado.objects.filter(pk=self.teclado.id)
        placabase = PlacaBase.objects.filter(pk=self.placabase.id)
        cpu = CPU.objects.filter(pk=self.cpu.id)
        altavoz = Altavoz.objects.filter(pk=self.altavoz.id)
        components = (monitor, raton, teclado, placabase, cpu, altavoz)
        return components

    def save(self, *args, **kwargs):
        """ Comprobar si actualiza """
        if('update' in kwargs and kwargs['update'] == True):
            print('Actualizando...')
            return super(Computadora, self).save()
        """ Obtener todos los componentes """
        components = self.get_components()
        no_stock_message = "No stock: "
        there_is_stock = True

        """ Cantidad de computadoras mayor a 0 """
        if(self.cantidad < 1):
            raise ValidationError('Cantidad menor a 1')

        """ Verificando stock de cada componente"""
        for component in components:
            if not (len(component) > 0 and component[0].stock >= self.cantidad):
                no_stock_message += f'{component[0].__str__()}  '
                there_is_stock = False

        """ Si existe stock de todos los componentes """
        if there_is_stock:
            """ Restando stock y calculando el costo de al computadora """
            costo = 0
            for component in components:
                component.update(stock=models.F('stock') - self.cantidad)
                costo += component[0].costo

            self.costo = costo

            return super(Computadora, self).save(*args, **kwargs)
        else:
            raise ValidationError(no_stock_message)

    def __str__(self) -> str:
        return f'{self.nombre} Q{self.costo} ({self.cantidad})'