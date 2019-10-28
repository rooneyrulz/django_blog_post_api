from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken

from django.contrib.auth.models import User
from .serializers import (
  UserSerializer,
  RegisterSerializer,
  LoginSerializer
)


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
