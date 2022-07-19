from django.shortcuts import render

from rest_framework import viewsets

from .serializers import UserSerializer, ProfileSerializer
from .models import User, Profile


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer