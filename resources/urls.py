from django.urls import path
from .views import ResourceListView, ResourceCreationView, ResourceDetailView, ResourceUpdateView

app_name = "resources"

urlpatterns = [
    path("", view=ResourceListView.as_view(), name='resources'),
    path("create/", view=ResourceCreationView.as_view(), name="create"),
    path("<slug:slug>/", view=ResourceDetailView.as_view(), name="detail"),
    path("<slug:slug>/update/", view=ResourceUpdateView.as_view(), name="update"),
]
