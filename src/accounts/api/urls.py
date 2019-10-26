from django.urls import path
from .views import RegisterAPIView

urlpatterns = [
  path(
    'register',
    RegisterAPIView.as_view(),
    name='register-api-view'
  ),
  # path(
  #   'blog-posts/<int:pk>/detail',
  #   DetailUpdateDeleteAPIView.as_view(),
  #   name='detail-update-delete-api-view'
  # )
]