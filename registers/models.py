from django.db import models
#Models
from plants.models import Plants

# Create your models here.

class Registry(models.Model):
    '''Registry models'''
    plant = models.ForeignKey(Plants, on_delete=models.CASCADE, null=True)

    week_control = models.DateTimeField(blank=True)

    water_consuption = models.FloatField(default=0)

    size_control = models.FloatField(default=0)

    picture = models.ImageField(upload_to='registers/picture',
                                height_field=None,
                                width_field=None,
                                max_length=None,
                                blank=True,
                                null=True
                                )

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-created']