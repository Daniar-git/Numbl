from rest_framework import generics
from rest_framework.generics import RetrieveAPIView

from .models import Videodetails
from .serializers import WatchSerializers


class WatchVideoAPIView(RetrieveAPIView):
    queryset = Videodetails.objects.all()
    serializer_class = WatchSerializers

class VideoUploadView(generics.CreateAPIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)