from django.contrib import admin

from .models import Raton, Teclado, Monitor, Orden, Computadora

""" Registrando modelos al admin """
admin.site.register(Raton)
admin.site.register(Teclado)
admin.site.register(Monitor)
admin.site.register(Orden)
admin.site.register(Computadora)
