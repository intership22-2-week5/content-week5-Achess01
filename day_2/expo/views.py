from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ExpoDateSerializer, AuthorSerializer, ArtworkSerializer, PortfolioSerializer, ExpoSerializer, MultimediaSerializer
from .models import ExpoDate, Author, Artwork, Portfolio, Expo, Multimedia


class ExpoDateViewSet(viewsets.ModelViewSet):
    queryset = ExpoDate.objects.all()
    serializer_class = ExpoDateSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class ExpoViewSet(viewsets.ModelViewSet):
    queryset = Expo.objects.all()
    serializer_class = ExpoSerializer


class MultimediaViewSet(viewsets.ModelViewSet):
    queryset = Multimedia.objects.all()
    serializer_class = MultimediaSerializer
