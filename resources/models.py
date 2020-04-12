from django.conf import settings
from django.db import models
from core.models import TimeStampedModel
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from django.urls import reverse


class AbstractItem(TimeStampedModel):

    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Resources(TimeStampedModel):

    RESOURCE_TYPES = (
        ('blog_post', 'Blog Post'),
        ('youtube', 'Youtube'),
        ('website', 'Website'),
        ('book', 'Book'),
    )

    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(
        "users.User", related_name="resources", on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(default="")
    tags = TaggableManager()
    resource_type = models.CharField(
        max_length=50, choices=RESOURCE_TYPES, null=True, blank=True)
    thumbnail = models.URLField(max_length=200, null=True)
    slug = AutoSlugField("Resource Address",
                         null=True,
                         unique=True, always_update=False, populate_from="title")

    def get_all_comments(self):
        all_comments = self.comments.all().count()
        return all_comments

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:home")
