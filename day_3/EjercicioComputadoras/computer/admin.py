# Django
from django.contrib import admin

# Models
from .models.components import Raton, Teclado, Monitor, PlacaBase, CPU, Altavoz
from .models.computer import Computadora
from .models.order import Orden

""" Registrando modelos al admin """
admin.site.register(Raton)
admin.site.register(Teclado)
admin.site.register(Monitor)
admin.site.register(Orden)
admin.site.register(Computadora)
admin.site.register(PlacaBase)
admin.site.register(CPU)
admin.site.register(Altavoz)
