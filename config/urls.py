from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("resources/", include("resources.urls")),
    path("comments/", include("comments.urls")),
    path('admin/', admin.site.urls),
]