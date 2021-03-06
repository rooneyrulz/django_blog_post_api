from django.urls import path
from .views import ListCreateAPIView, DetailUpdateDeleteAPIView

app_name = 'blog_posts'
urlpatterns = [
  path(
    'blog-posts',
    ListCreateAPIView.as_view(),
    name='list-create-api-view'
  ),
  path(
    'blog-posts/<int:pk>/detail',
    DetailUpdateDeleteAPIView.as_view(),
    name='detail-update-delete-api-view'
  )
]