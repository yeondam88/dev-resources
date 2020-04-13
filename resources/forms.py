from django import forms
from . import models
from taggit.forms import TagWidget


class ResourceForm(forms.ModelForm):

    class Meta:
        model = models.Resources
        fields = ("title", "description", "tags", "resource_type", "thumbnail", "url")

    def save(self, *args, **kargs):
        resource = super().save(commit=False)
        return resource
