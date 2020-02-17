from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    '''users profile'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return username'''
        return self.user.username