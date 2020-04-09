from django import forms
from . import models


class ResourceForm(forms.ModelForm):

    class Meta:
        model = models.Resources
