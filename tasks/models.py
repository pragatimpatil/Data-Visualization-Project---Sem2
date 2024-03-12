from django.db import models

# Create your models here.
class task(models.Model):
  agnname = models.CharField(max_length=255)
  
class voption(models.Model):
  plotname = models.CharField(max_length=255)
  
class module(models.Model):
  name = models.CharField(max_length=255)

