from rest_framework import serializers
from .models import Videodetails

class WatchSerializers(serializers.Serializer):
    class Meta:
        model = Videodetails
        fields = ['title', 'description','video_file' ,'likes','dislikes','views', 'upload_date', 'comments', 'duration']

class UploadSerilizers(serializers.Serializer):
    class Meta:
        model = Videodetails
        fields = ['title','description','video_file','upload_date','duration','tags','category','uploader']
