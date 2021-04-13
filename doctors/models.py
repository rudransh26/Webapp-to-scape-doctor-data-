from django.db import models

class entry(models.Model):
    city = models.CharField(max_length=50)
    specialization =models.CharField(max_length=50)