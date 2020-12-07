from django.urls import path

from .views import homepage, infopage


urlpatterns = [
    path('', homepage, name='home'),
    path('info/', infopage, name='info'),
]
