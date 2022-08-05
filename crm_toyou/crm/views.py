from django.shortcuts import render
from django.views.generic import ListView

from .models import Project


class HomeProjects(ListView):
    model = Project
    template_name = 'crm/index.html'
    context_object_name = 'projects'


def index(request):
    return render(request, 'crm/index.html')
