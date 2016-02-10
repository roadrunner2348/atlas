from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy

#Program Class Based Views

class ProgramIndex(ListView):
    model = Program

class ProgramDetailView(DetailView):
    model = Program

class ProgramCreate(CreateView):
    model = Program
    fields = ['name']

class ProgramUpdate(UpdateView):
    model = Program
    fields = ['name']

class ProgramDelete(DeleteView):
    model = Program
    success_url = reverse_lazy('inventory:program_index')

##Client Class Based Views

class ClientIndex(ListView):
    model = Client

class ClientDetailView(DetailView):
    model = Client

class ClientCreate(CreateView):
    model = Client
    fields = ['username', 'full_name', 'year_of_graduation', 'is_student', 'program']

class ClientUpdate(UpdateView):
    model = Client
    fields = ['username', 'full_name', 'year_of_graduation', 'is_student', 'program']

class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('inventory:client_index')
