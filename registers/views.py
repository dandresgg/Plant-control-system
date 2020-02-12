from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
#Forms
from registers.forms import RegisterForm
#Models
from registers.models import Registry

# Create your views here.


class RegisterPlants(FormView):
    '''create a plats register'''
    template_name = 'registers/new_register.html'
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        '''Add users post to context'''
        context = super().get_context_data(**kwargs)
        register = Registry.objects.all()
        context['register'] = register[1]
        context['registers'] = register
        return context

    def form_valid(self, form):
        '''save form data'''
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('registers:new_register')