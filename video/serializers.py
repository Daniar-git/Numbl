from rest_framework import serializers
from .models import Videodetails,Categories

class WatchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videodetails
        fields = ['title', 'description','video_file' ,'likes','dislikes','views', 'upload_date', 'comments', 'duration']

class UploadSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Videodetails
        fields = ['title','description','video_file','upload_date','duration','tags','category']

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['category_id']

class AllCategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'