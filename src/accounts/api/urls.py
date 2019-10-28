from django.urls import path
from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
  path(
    'register',
    RegisterAPIView.as_view(),
    name='register-api-view'
  ),
  path(
    'login',
    LoginAPIView.as_view(),
    name='login-api-view'
  )
]