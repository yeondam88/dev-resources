from django import forms
from . import models


class CommentForm(forms.ModelForm):

    comment = forms.CharField(max_length=255)

    class Meta:
        model = models.Comments
        fields = ("comment",)

    def save(self):
        comment = super().save(commit=False)
        return comment
