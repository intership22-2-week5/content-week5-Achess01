from django.db import models
from user.models import Profile


class ExpoDate(models.Model):
    day = models.DateField()

    def __str__(self) -> str:
        return f'{self.day}'


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.name} <{self.email}>'


class Artwork(models.Model):
    type = models.CharField(max_length=50)
    creation_date = models.DateField()
    price = models.FloatField()
    authors = models.ManyToManyField(Author)

    def __str__(self) -> str:
        return f'Type: {self.type} Q{self.price}'


class Portfolio(models.Model):
    description = models.CharField(max_length=255)
    artworks = models.ManyToManyField(Artwork)

    def __str__(self) -> str:
        return f'Porfolio: {self.description}'


class Expo(models.Model):
    dates = models.ManyToManyField(ExpoDate)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    portfolios = models.ManyToManyField(Portfolio)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Info: {self.description}'


class Multimedia(models.Model):
    type = models.CharField(max_length=50)
    uri = models.CharField(max_length=255)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Type: {self.type} URL: {self.uri}'
