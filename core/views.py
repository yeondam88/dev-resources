from django.shortcuts import render
from resources.models import Resources


def index(request):

    resources = Resources.objects.all()

    context = {
        'resources': resources
    }

    return render(request, 'pages/home.html', context)
