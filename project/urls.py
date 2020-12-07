from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('books/', include('books.urls')),
    path('journals/', include('journals.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
