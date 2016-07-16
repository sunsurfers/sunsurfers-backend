from django.conf.urls import url

from surfers import views


urlpatterns = [
    url(r'^$', views.sunmap, name='sunmap'),
    url(r'^latest$', views.latest, name='latest_geojson'),
]
