from django.db import models

# Create your models here.

class Plants(models.Model):
    '''plants models'''
    plant_name = models.CharField(max_length=20, null=True)

    plant_class = models.CharField(max_length=40, null=True)

    plant_type = models.CharField(max_length=20, null=True)

    active_nutrients = models.FloatField(default=0)
    
    noactive_nutrients = models.FloatField(default=0)

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plant_name
