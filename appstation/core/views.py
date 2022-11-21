from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from models import Setting

class SettingsCreateView(CreateView):
    model = Setting

class SettingsListView(ListView):
    model = Setting

class SettingsUpdateView(UpdateView):
    model = Setting
    
class SettingsDeleteView(DeleteView):
    model = Setting
    
class SettingsDetailView(DetailView):
    model = Setting
    
class indexView(TemplateView):
    template_name = 'index.html'
