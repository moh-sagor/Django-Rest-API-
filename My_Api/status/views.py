from .models import Status
from .serializers import StatusSerializer

from rest_framework import generics, parsers

# Create your views here.


class StatusListCreateView(  # mixins.CreateModelMixin,
        generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class StatusDetailUpdateDeleteAPIView(  # mixins.UpdateModelMixin, mixins.DestroyModelMixin,
        generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
