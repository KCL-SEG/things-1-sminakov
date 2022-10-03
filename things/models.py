from django.db import models

class Thing(models.Model):
    name = models.CharField(models.Model)
    description = models.TextField()
    quantity = models.IntegerField()