from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView, DetailView, UpdateView, View
from .models import Resources
from comments.models import Comments
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
    template_name = 'resources/resources_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        resource = Resources.objects.get(slug=slug)
        comments = Comments.objects.filter(
            parent__isnull=True, resource=resource)
        context['comments'] = comments
        return context


class ResourceUpdateView(UpdateView):

    model = Resources
    template_name = 'resources/resources_update.html'
    fields = (
        'title',
        'description',
        'thumbnail',
        'url',
        'tags'
    )
