from django.urls import path

from surfers import views


urlpatterns = [
    path('', views.sunmap, name='sunmap'),
    path('latest', views.latest, name='latest_geojson'),
]
