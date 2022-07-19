
from django.db import router

# Django rest framework
from rest_framework.routers import DefaultRouter

# Views
from .views import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = router.urls

urlpatterns += []
