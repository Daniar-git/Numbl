from rest_framework import serializers
from .models import Userdata

class LoginSerializers(serializers.Serializer):
    class Meta:
        model = Userdata
        fields= ['username','password']

class RegistrationSerializers(serializers.Serializer):
    class Meta:
        model = Userdata
        exclude =('user_id',)