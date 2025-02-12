from django.db import models
from django.utils import timezone

# Create your models here.abs
class appOneModel(models.Model):
    APP_TYPE=[
        ('IND', 'INDIGO'),
        ('LST', 'LOST'),
        ('CMP', 'COMPASS'),
        ('PND', 'PANDORA'),
    ]
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='appOne/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=4, choices=APP_TYPE) 