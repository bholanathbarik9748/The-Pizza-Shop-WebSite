from django.db import models

# Create your models here.

# class


class item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
