from django.urls import path
from .views import ResourceListView, ResourceCreationView

app_name = "resources"

urlpatterns = [
    path("", view=ResourceListView.as_view(), name='resources'),
    path("create/", view=ResourceCreationView.as_view(), name="create"),
]
