from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView


from resources.models import Resources
from .serializers import ResoucesSerializer


class ResourceCreateAPIView(CreateAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResoucesSerializer


class ResourceListAPIView(ListAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResoucesSerializer


class ResourceDetailAPIView(RetrieveAPIView):
    queryset = Resources.objects.all()
    serializer_class = ResoucesSerializer


class ResourceUpdateAPIView(RetrieveUpdateAPIView
                            ):
    queryset = Resources.objects.all()
    serializer_class = ResoucesSerializer


class ResourceDeleteAPIView(RetrieveDestroyAPIView
                            ):
    queryset = Resources.objects.all()
    serializer_class = ResoucesSerializer
