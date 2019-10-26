from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import BlogPostSerializer
from blog_posts.models import BlogPost

class ListCreateAPIView(APIView):
  model = BlogPost
  serializer = BlogPostSerializer

  def get(self, request, *args, **kwargs):
    qs = self.model.objects.all()
    serializer = self.serializer(qs, many=True)
    return Response(serializer.data, status=200)

  def post(self, request, *args, **kwargs):
    serializer = self.serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)


class DetailUpdateDeleteAPIView(APIView):
  model = BlogPost
  serializer = BlogPostSerializer

  def get_object(self, id):
    return get_object_or_404(self.model, pk=id)
  
  def get(self, request, pk=None, *args, **kwargs):
    obj = self.get_object(pk)
    serializer = self.serializer(obj)
    return Response(serializer.data, status=200)

  def put(self, request, pk=None, *args, **kwargs):
    obj = self.get_object(pk)
    serializer = self.serializer(obj, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=200)

  def delete(self, request, pk=None, *args, **kwargs):
    obj = self.get_object(pk)
    obj.delete()
    return Response('Blog post deleted successfully!', status=200)

