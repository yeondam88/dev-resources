from django.urls import path
from .views import ResourceListView

urlpatterns = [
    path('', view=ResourceListView.as_view(), name='resources')
]
