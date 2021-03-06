"""sunsurfers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib.gis import admin

from surfers.api import v1_api

from . import auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1_api.urls)),
    path('tg/', include('tgauth.urls')),
    path('', include('surfers.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('register-by-token/<backend>/', auth.register_by_access_token, 'register_by_access_token'),
]
