#Django
from django.urls import path
#views
from . import views

urlpatterns = [
    path(
        route = '',
        view = views.ListPlants.as_view(),
        name = 'plants'
    ),
    path(
        route = 'plants/add/',
        view = views.CreatePlants.as_view(),
        name = 'new_plant'
    ),
    path(
        route = 'registers/new/<int:id>/',
        view = views.PlantDetails.as_view(),
        name = 'plant_details'
    )

]