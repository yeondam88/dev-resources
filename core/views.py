from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, View
from resources.models import Resources
from django.urls import reverse


class IndexView(ListView):

    model = Resources
    template_name = 'pages/home.html'
    paginate_by = 6
    paginate_orphans = 5
    ordering = ["-created"]
    context_object_name = "resources"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TagsFilterView(View):

    def get(self, request, tag):
        if tag:
            resources = Resources.objects.filter(
                tags__name=tag).order_by("-created")
            if resources is not None:
                return render(request, "resources/resource_tags_result.html", {'resources': resources})
            else:
                return redirect(reverse("core:home"))
