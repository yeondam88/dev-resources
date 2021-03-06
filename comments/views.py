from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from .models import Comments
from .forms import CommentForm

from resources.models import Resources


def create_comment(request, slug):
    if request.method == "POST":
        form = CommentForm(request.POST)
        resource = Resources.objects.get_or_none(slug=slug)
        if not resource:
            return redirect(reverse("core:home"))
        if form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comments.objects.get(id=parent_id)
                if parent_obj:
                    reply_comment = form.save()
                    reply_comment.parent = parent_obj

            comment = form.save()
            comment.resource = resource
            comment.user = request.user
            comment.save()
            return redirect(reverse("resources:detail", kwargs={"slug": resource.slug}))

    else:
        form = CommentForm()

    return redirect(reverse("core:home"))
