#Django
from django.urls import path
#views registers
from registers import views

urlpatterns = [
    path (
        route='',
        view=views.RegisterPlants.as_view(),
        name='new_register'
    )
]