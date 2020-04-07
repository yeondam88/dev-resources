from django.shortcuts import render
from django.views.generic import ListView
from .models import Resources


class ResourceListView(ListView):

    model = Resources
