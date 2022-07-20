from statistics import mode
from django.db import models
""" Una orden contiene a todas las computadoras """


""" Dispositivo de entrada """


class DispositivoEntrada(models.Model):
    entrada = models.CharField(max_length=50)
    marca = models.CharField(max_length=255)
    stock = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.entrada} ({self.marca})'


class Raton(DispositivoEntrada):

    def __str__(self) -> str:
        return f'Ratón {super().__str__()}'


class Teclado(DispositivoEntrada):

    def __str__(self) -> str:
        return f'Teclado {super().__str__()}'


class Monitor(models.Model):
    tamanio = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    stock = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f'Monitor {self.tamanio} ({self.marca})'


class Computadora(models.Model):
    nombre = models.CharField(max_length=255)
    monitor = models.ForeignKey(
        Monitor, on_delete=models.SET_NULL, null=True)
    raton = models.ForeignKey(Raton, on_delete=models.SET_NULL, null=True)
    teclado = models.ForeignKey(
        Teclado, on_delete=models.SET_NULL, null=True)
    disponible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """ Reducir stocks al crear computadora """
        monitor = Monitor.objects.filter(pk=self.monitor.id)
        raton = Raton.objects.filter(pk=self.raton.id)
        teclado = Teclado.objects.filter(pk=self.teclado.id)

        if (
            len(monitor) > 0 and monitor[0].stock > 0
            and
            len(raton) > 0 and raton[0].stock > 0
            and
            len(teclado) > 0 and teclado[0].stock > 0
        ):
            monitor.update(stock=models.F('stock') - 1)
            raton.update(stock=models.F('stock') - 1)
            teclado.update(stock=models.F('stock') - 1)            
            super(Computadora, self).save(*args, **kwargs)
        else:
            return

    def __str__(self) -> str:
        return f'{self.nombre}'


class Orden(models.Model):
    description = models.CharField(max_length=255, default="Orden")
    computadoras = models.ManyToManyField(Computadora)

    def __str__(self) -> str:
        return f'{self.description}'
