from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('blog_posts.api.urls')),
    path('api/', include('accounts.api.urls')),
    path('admin/', admin.site.urls),
]
