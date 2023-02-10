from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializers, RegistrationSerializers
from .models import Userdata




class UserRegistrationView(CreateAPIView):
    model = Userdata
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializers
#   Cheking
#   Hashing
#   Userdata.save()

class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = Userdata.objects.filter(email=email, password=password).first()

        if user:
            return Response({"message": "Login successful"})
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)