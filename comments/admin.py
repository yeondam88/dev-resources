from django.contrib import admin
from .models import Comments


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass
