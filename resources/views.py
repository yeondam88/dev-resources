import random
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView, DetailView, UpdateView, View
from .models import Resources
from comments.models import Comments
from . import forms
from django.contrib import messages


RANDOM_IMAGE_URL = 'https://source.unsplash.com/1600x900/?'
RANDON_COLLECTION_KEYWORD = ['macbook', 'programming', 'iphone', 'dev', 'computer', 'software']

class ResourceListView(ListView):

    model = Resources
    context_object_name = 'resources'


class ResourceCreationView(LoginRequiredMixin, FormView):

    login_url = '/users/login/'
    form_class = forms.ResourceForm
    template_name = "resources/resources_create.html"

    def form_valid(self, form):
        user = self.request.user
        tags = form.cleaned_data.get("tags")
        url = form.cleaned_data.get('url')
        thumbnail = form.cleaned_data.get('thumbnail')
        resource = form.save()
        if thumbnail is None:
            resource.thumbnail = RANDOM_IMAGE_URL + random.choice(RANDON_COLLECTION_KEYWORD)
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


class ResourceUpdateView(LoginRequiredMixin, UpdateView):

    model = Resources
    template_name = 'resources/resources_update.html'
    login_url = '/users/login/'
    fields = (
        'title',
        'description',
        'thumbnail',
        'url',
        'tags'
    )
