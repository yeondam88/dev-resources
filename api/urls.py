from django.urls import path
from .views import ResourceListAPIView, ResourceDetailAPIView, ResourceCreateAPIView, ResourceUpdateAPIView, ResourceDeleteAPIView

urlpatterns = [
    path('', ResourceListAPIView.as_view()),
    path('create', ResourceCreateAPIView.as_view()),
    path('<int:pk>/', ResourceDetailAPIView.as_view()),
    path('<int:pk>/update/', ResourceUpdateAPIView.as_view()),
    path('<int:pk>/delete/', ResourceDeleteAPIView.as_view()),
]
