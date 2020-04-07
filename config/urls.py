from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("resources/", include("resources.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
