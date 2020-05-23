from django.contrib import admin

# Register your models here.
from .models import Registry

@admin.register(Registry)
class RegistryAdmin(admin.ModelAdmin):
    list_display = ('week_control','water_consuption',\
                    'size_control','picture','created','modified')
    list_filters = ('created','modified')
    search_fields = ('week_control','water_consuption','size_control')



