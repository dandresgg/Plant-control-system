#Django
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, FormView, TemplateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
#Forms
from .forms import PlantsFormat
from registers.forms import RegisterForm
#Models
from registers.models import Registry
from .models import Plants
# Create your views here.

class ListPlants(LoginRequiredMixin, TemplateView):
    '''showing plants'''
    template_name = 'plants/home.html'
    success_url = reverse_lazy('plants:plants')

    def get_context_data(self, **kwargs):
        '''retuning context'''
        context = super().get_context_data(**kwargs)
        context['plants'] = Plants.objects.all()
        context['form'] = PlantsFormat()
        return context

class CreatePlants(LoginRequiredMixin, FormView):
    '''creating plants'''
    template_name = 'plants/new.html'
    form_class = PlantsFormat

    def form_valid(self, form):
        '''save form plants data'''
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('plants:plants')

class PlantDetails(LoginRequiredMixin, DetailView, FormView):
    '''plants's details'''
    template_name = 'registers/new_register.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    queryset = Plants.objects.all()
    context_object_name = 'id'
    form_class = RegisterForm

    def get_context_data(self, *args, **kwargs):
        '''Add users post to context'''
        plant = self.get_object()
        registers = Registry.objects.filter(plant=plant)
        context = {
            'plant': self.get_object(),
            'registers' : registers,
            'form' : RegisterForm()
        }
        return context

    def form_valid(self, form):
        '''save form plant detail data'''
        plant = self.get_object()
        register = form.save(commit=False)
        register.plant = plant
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        plant = self.get_object()
        return reverse_lazy('plants:plant_details', kwargs={'id':plant.id})