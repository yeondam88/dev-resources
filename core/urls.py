from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', view=views.IndexView.as_view(), name='home'),
    path('tags/<str:tag>/', view=views.TagsFilterView.as_view(), name='tags')
]
