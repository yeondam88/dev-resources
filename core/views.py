from django.shortcuts import render
from django.views.generic import ListView
from resources.models import Resources


class IndexView(ListView):

    model = Resources
    template_name = 'pages/home.html'
    paginate_by = 6
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "resources"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
