from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("create/<slug:slug>/", views.create_comment, name="create")
]
