from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, View
from resources.models import Resources
from django.urls import reverse
from .forms import SearchForm
from django.core.paginator import Paginator


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


class ResourceSearchResultView(View):

    def get(self, request):

        term = request.GET.get('term')

        if term:

            form = SearchForm(request.GET)
            if form.is_valid():

                term = form.cleaned_data.get('term')

                filter_args = {}

                if term != 'JavaScript'.lower():
                    filter_args['title__icontains'] = term

                qs = Resources.objects.filter(
                    **filter_args).order_by('-created')

                paginator = Paginator(qs, 10, orphans=5)
                page = request.GET.get('page', 1)
                resources = paginator.get_page(page)

                print(qs)

                return render(
                    request, "resources/resources_search_result.html",
                    {"form": form, "resources": resources}
                )
        else:
            form = SearchForm()

        return render(request, "resources/resources_search_result.html", {"form": form})
