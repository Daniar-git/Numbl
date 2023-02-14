import requests
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Videodetails,Categories
from .serializers import WatchSerializers, UploadSerilizers, AllCategoriesSerializers


# class WatchVideoAPIView(generics.RetrieveAPIView):
#     queryset = Videodetails.objects.all()
#     serializer_class = WatchSerializers
#
# class VideoUploadView(generics.CreateAPIView):
#     queryset = Videodetails.objects.all()
#     serializer_class = UploadSerilizers
#
#     def create(self, request, *args, **kwargs):
#         Set the desired value for the field here
        # category_name = request.data.get('category_name')
        # if category_name:
        #     response = requests.get('http://localhost:8000/category/' + category_name)
        #     category_id = response.get('category_id')
        #     request.data['category'] = category_id
        #
        # return super().create(request, *args, **kwargs)
#
#
# class CategoryAPIView(APIView):
#     queryset = Categories.objects.all()
#     def get(self, request, name):
#         category = Categories.objects.filter(name=name).first()
#         if not category:
#             return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
#         return Response({'category_id': category.category_id})
#
# class CategoryListAPIView(generics.ListAPIView):
#     queryset = Categories.objects.all()
#     serializer_class = AllCategoriesSerializers
#
