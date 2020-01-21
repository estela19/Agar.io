from django.db import models
from django.conf import settings


class Player(models.Model):
    objects = models.Manager()
    name = models.TextField(max_length=20)
    posX = models.FloatField
    posY = models.FloatField
    radius = models.FloatField
    color = models.CharField(max_length=7)

class Food(models.Model):
    objects = models.Manager()
    posX = models.FloatField
    posY = models.FloatField
    radius = models.FloatField
    color = models.CharField(max_length=7)