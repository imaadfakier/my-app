from django.db import models

# Create your models here.
class Restaurant(models.Model):
    '''...'''

    # ...

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=10, default='')
    rating = models.FloatField(null=False, default=0.00)
