from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView, DetailView
from .models import Resources
from . import forms
from django.contrib import messages


class ResourceListView(ListView):

    model = Resources
    context_object_name = 'resources'


class ResourceCreationView(FormView):

    form_class = forms.ResourceForm
    template_name = "resources/resources_create.html"

    def form_valid(self, form):
        user = self.request.user
        tags = form.cleaned_data.get("tags")
        url = form.cleaned_data.get('url')
        resource = form.save()
        resource.author = user
        resource.save()
        for tag in tags:
            resource.tags.add(tag)
        resource.save()

        return redirect(reverse("core:home"))


class ResourceDetailView(DetailView):

    model = Resources
    context_object_name = 'resource'
