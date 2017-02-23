from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout)
]
