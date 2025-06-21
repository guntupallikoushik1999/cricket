from django.db import models
from django.contrib import admin

# Create your models here.
class Bowler(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=100)
    wickets_taken = models.IntegerField()
    bowling_average = models.FloatField()
    bowling_strikerate = models.FloatField()
    economy_rate = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.country})"
