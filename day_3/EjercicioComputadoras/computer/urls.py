from django.db import router

from rest_framework.routers import DefaultRouter

from .views import RatonViewSet, TecladoViewSet, MonitorViewSet, OrdenViewSet, ComputadoraViewSet, PlacaBaseViewSet, CPUViewSet, AltavozViewSet

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
