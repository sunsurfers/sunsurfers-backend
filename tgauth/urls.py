from django.urls import path

from tgauth import views


urlpatterns = [
    path('webhook/<token>', views.botapi, name='webhook'),
    path('login/<token>', views.login, name='login'),
]
