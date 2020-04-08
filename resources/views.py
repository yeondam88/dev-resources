from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Resources
from django.contrib import messages


class ResourceListView(ListView):

    model = Resources


class ResourceCreationView(CreateView):

    model = Resources
    fields = [
        "title",
        "description",
        "tags",
        "resource_type",
        "thumbnail"
    ]

    def form_valid(self, form):
        resource = form.save()
        resource.author = self.request.user
        resource.save()
        messages.success(self.request, "Resource created!")
        return redirect(reverse("core:home"))
