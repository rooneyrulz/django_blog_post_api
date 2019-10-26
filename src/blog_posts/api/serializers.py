from rest_framework import serializers
from blog_posts.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = BlogPost
    fields = ['id', 'title', 'body', 'author', 'created_at']

  def validate_title(self, value):
    qs = BlogPost.objects.filter(title__iexact=value)
    if qs.exists():
      raise serializers.ValidationError('title has already been used!')
    return value

  def validate_body(self, value):
    qs = BlogPost.objects.filter(body__iexact=value)
    if qs.exists():
      raise serializers.ValidationError('post body has already been used!')
    return value