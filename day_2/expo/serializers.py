from rest_framework import serializers

from .models import ExpoDate, Author, Artwork, Portfolio, Expo, Multimedia


class ExpoDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpoDate
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = '__all__'        


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'        


class ExpoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expo
        fields = '__all__'
        


class MultimediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Multimedia
        fields = '__all__'
