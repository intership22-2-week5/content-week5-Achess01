from django.db import models
from django.forms import ValidationError

""" Una orden contiene a todas las computadoras """


""" Dispositivo de entrada """


class Componente(models.Model):
    class Meta:
        abstract = True
    tipo = models.CharField(max_length=255, default='Componente')
    marca = models.CharField(max_length=255)
    costo = models.FloatField(default=0)
    stock = models.IntegerField(default=1)
    descripcion = models.CharField(max_length=255, default="Componente")
    fecha_ingreso = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f'({self.marca}) ({self.stock})'


class DispositivoSalida(Componente):
    class Meta:
        abstract = True


class DispositivoInterno(Componente):
    class Meta:
        abstract = True


class DispositivoEntrada(Componente):
    entrada = models.CharField(max_length=50, default='usb')

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.entrada} {super().__str__()}'


class Raton(DispositivoEntrada):

    def __str__(self) -> str:
        return f'Ratón {super().__str__()}'


class Teclado(DispositivoEntrada):

    def __str__(self) -> str:
        return f'Teclado {super().__str__()}'


class Monitor(DispositivoSalida):
    tamanio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Monitor {self.tamanio} {super().__str__()}'


class Altavoz(DispositivoSalida):

    def __str__(self) -> str:
        return f'Altavoz {super().__str__()}'


class CPU(DispositivoInterno):

    def __str__(self) -> str:
        return f'CPU {super().__str__()}'


class PlacaBase(DispositivoInterno):

    def __str__(self) -> str:
        return f'Placa Madre {super().__str__()}'


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

            super(Computadora, self).save(*args, **kwargs)
        else:
            raise ValidationError(no_stock_message)

    def __str__(self) -> str:
        return f'{self.nombre}'


class Orden(models.Model):
    description = models.CharField(max_length=255, default="Orden")
    computadoras = models.ManyToManyField(Computadora)

    def __str__(self) -> str:
        return f'{self.description}'
