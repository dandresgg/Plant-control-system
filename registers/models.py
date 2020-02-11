from django.db import models

# Create your models here.

Class Registry(models.Model):
    '''Registry models'''
    plant_name = models.CharField(max_lengh=20)

    week_control = models.DateTimeField(blank=True)

    water_consuption = models.FloatField(default=0)

    active_nutrients = models.FloatField(default=0)
    noactive_nutrients = models.FloatField(default=0)

    size_control = models.FloatField(default=0)

    picture = models.ImageField(upload_to='registers/picture',
                                height_field=200,
                                width_field=200,
                                max_lengh=None,
                                blank=True,
                                null=True
                                )

    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)