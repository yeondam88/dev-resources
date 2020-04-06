from django.contrib import admin
from . import models


@admin.register(models.Resources)
class ResourcesAdmin(admin.ModelAdmin):
    pass
