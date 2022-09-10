from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=5, choices=Genre.choices)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    


    def __str__ (self):
        return f"{self.name}"


class Listing(models.Model):
    class Type(models.TextChoices):
        Records = "Disques"
        Clothing = "Vêtements"
        Posters = "Affiches"
        Miscellaneous = "Divers"
    name = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])
    like_new = models.fields.BooleanField(default=False)

    band = models.ForeignKey(Band, null = True, on_delete=models.SET_NULL)
    
    
    def __str__ (self):
        return f"{self.name}"