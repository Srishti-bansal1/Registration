from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length = 100)
    dob = models.DateField()
    email = models.EmailField()
    state = models.CharField(max_length = 100 )
    city = models.CharField(max_length = 100)
    pin = models.IntegerField()

    
    
    
