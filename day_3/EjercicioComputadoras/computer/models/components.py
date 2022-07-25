from django.db import models


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
