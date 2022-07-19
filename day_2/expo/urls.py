from django.urls import path
from django.db import router

from rest_framework.routers import DefaultRouter

from .views import ExpoDateViewSet, AuthorViewSet, ArtworkViewSet, PortfolioViewSet, ExpoViewSet, MultimediaViewSet

router = DefaultRouter()

router.register(r'dates', ExpoDateViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'artworks', ArtworkViewSet)
router.register(r'portfolios', PortfolioViewSet)
router.register(r'expos', ExpoViewSet)
router.register(r'multimedias', MultimediaViewSet)

urlpatterns = router.urls

urlpatterns += []
