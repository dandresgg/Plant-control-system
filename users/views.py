#Django views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
# Create your views here.


class LoginView(auth_views.LoginView):
    '''users login'''
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    '''logout users'''
    template_name = 'users/logout'