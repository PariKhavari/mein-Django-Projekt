from django.db import models

# Create your models here.


class Fdata(models.Model):
    name = models.CharField(max_length=255)
    # weight = models.FloatField()

