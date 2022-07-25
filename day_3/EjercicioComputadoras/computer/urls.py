# Django
from django.db import router

# Rest framework
from rest_framework.routers import DefaultRouter

# Viewsets
from .viewsets.components import RatonViewSet, TecladoViewSet, MonitorViewSet, PlacaBaseViewSet, CPUViewSet, AltavozViewSet
from .viewsets.computer import ComputadoraViewSet
from .viewsets.order import OrdenViewSet

router = DefaultRouter()

""" Registrando rutas usando las views """
router.register(r'ratones', RatonViewSet)
router.register(r'teclados', TecladoViewSet)
router.register(r'monitores', MonitorViewSet)
router.register(r'ordenes', OrdenViewSet)
router.register(r'computadoras', ComputadoraViewSet)
router.register(r'placas', PlacaBaseViewSet)
router.register(r'cpus', CPUViewSet)
router.register(r'altavoz', AltavozViewSet)

""" Agregando las urls del router a los urlspatterns """
urlpatterns = router.urls

""" Agregando otras urls """
urlpatterns += []
