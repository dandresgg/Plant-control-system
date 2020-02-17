#Django
from django.urls import path
#views
from . import views

urlpatterns = [
    path(
        route='users/login/',
        view = views.LoginView.as_view(),
        name = 'login'
    ),
    path(
        route = 'users/logout/',
        view = views.LogoutView.as_view(),
        name = 'logout'
    ),

]