from django.db import router

from rest_framework.routers import DefaultRouter

from .views import RatonViewSet, TecladoViewSet, MonitorViewSet, OrdenViewSet, ComputadoraViewSet

router = DefaultRouter()

""" Registrando rutas usando las views """
router.register(r'ratones', RatonViewSet)
router.register(r'teclados', TecladoViewSet)
router.register(r'monitores', MonitorViewSet)
router.register(r'ordenes', OrdenViewSet)
router.register(r'computadoras', ComputadoraViewSet)

""" Agregando las urls del router a los urlspatterns """
urlpatterns = router.urls

""" Agregando otras urls """
urlpatterns += []
