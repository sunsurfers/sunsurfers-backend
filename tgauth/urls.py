from django.conf.urls import url

from tgauth import views


urlpatterns = [
    url(r'^webhook/(?P<token>.*)', views.botapi, name='webhook'),
    url(r'^login/(?P<token>.*)', views.login, name='login'),
]
