from django.db import models

# Create your models here.

# class

# Pizza


class item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)

# ANTIPASTO


class ANTIPASTO(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)

# BURGUR


class BURGUR(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)

# SAMOSA


class SAMOSA(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
