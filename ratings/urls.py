from django.conf.urls import patterns, url

from ratings import views

urlpatterns = patterns('',
    url(r'^(?P<id_number>\d+)/$', views.index, name='index'),
)
