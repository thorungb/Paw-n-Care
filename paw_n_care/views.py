from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Appointments(TemplateView):
    template_name = 'appointments.html'