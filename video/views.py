from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Videodetails,Categories
from .serializers import WatchSerializers, UploadSerilizers, CategorySerializers,AllCategoriesSerializers


class WatchVideoAPIView(generics.RetrieveAPIView):
    queryset = Videodetails.objects.all()
    serializer_class = WatchSerializers

class VideoUploadView(generics.CreateAPIView):
    queryset = Videodetails.objects.all()
    serializer_class = UploadSerilizers

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryAPIView(APIView):
    queryset = Categories.objects.all()

    def get(self, request, name):
        for name in len(Categories):

            PK = Categories.objects.get(name=name)
        serializer = CategorySerializers(PK)
        return Response(serializer.data)

class CategoryListAPIView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = AllCategoriesSerializers

