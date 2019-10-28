from django.urls import path
from .views import RegisterAPIView, LoginAPIView, GetUserAPIView

app_name = 'accounts'
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
  ),
  path(
    'user',
    GetUserAPIView.as_view(),
    name='user-api-view'
  )
]