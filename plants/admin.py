from django.contrib import admin

# Register your models here.

from .models import Plants

@admin.register(Plants)
class PlantsAdmin(admin.ModelAdmin):
    list_display = ('plant_name','plant_class','plant_type','active_nutrients','noactive_nutrients','created')
    list_filter = ('plant_class','plant_type','created')
    search_fields = ('plant_name','plant_type','plant_class')