from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeProjects.as_view(), name='home')
]