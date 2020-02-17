from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
#Forms
from registers.forms import RegisterForm
#Models
from registers.models import Registry

# Create your views here.
