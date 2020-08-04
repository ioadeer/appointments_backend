from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=100,blank=True, default='')
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    location = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey(get_user_model(), related_name='appointments', on_delete=models.CASCADE)
