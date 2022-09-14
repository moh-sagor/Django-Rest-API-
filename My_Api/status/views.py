from .models import Status
from .serializers import StatusSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, mixins

# Create your views here.


class StatusListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
