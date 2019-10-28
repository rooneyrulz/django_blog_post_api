from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken

from django.contrib.auth.models import User
from .serializers import (
  UserSerializer,
  RegisterSerializer,
  LoginSerializer
)


# REGISTER USER
class RegisterAPIView(APIView):
  serializer = RegisterSerializer
  model = User

  def post(self, request, *args, **kwargs):
    serializer = self.serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "token": AuthToken.objects.create(user)[1]
    })


# AUTHENTICATE USER
class LoginAPIView(APIView):
  serializer = LoginSerializer
  model = User

  def post(self, request, *args, **kwargs):
    serializer = self.serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    return Response({
      "token": AuthToken.objects.create(user)[1]
    })


# GET CURRENT USER
class GetUserAPIView(APIView):
  serializer = UserSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request, *args, **kwargs):
    user = request.user
    serializer = self.serializer(user)
    return Response(serializer.data, status=200)
