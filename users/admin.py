#Django
from django.contrib import admin
#models
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileADmin(admin.ModelAdmin):
    list_display = ('user',)
    list_filter = ('created', 'modified')