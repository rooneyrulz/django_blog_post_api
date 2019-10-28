from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        'api/',
        include(
            'blog_posts.api.urls',
            namespace='blog_posts'
        )
    ),
    path(
        'api/',
        include(
            'accounts.api.urls',
            namespace='accounts'
        )
    ),
    path('admin/', admin.site.urls),
]
