from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^user/register$', views.register),
    url(r'^user/login$', views.login),
    url(r'^user/logout$', views.logout),
    url(r'^user/success$', views.success),
]