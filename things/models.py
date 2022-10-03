from django.db import models

class Thing():
    name = models.CharField(models.Model)
    description = models.TextField()
    quantity = models.IntegerField()