from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']
    extra_kwargs = {'password': {'write_only': True}}
  
  def create(self, value):
    user = User.objects.create_user(**value)
    return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()
  