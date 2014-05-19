from django.conf.urls import patterns, url

from ratings import views

urlpatterns = patterns('',
    # url(r'^(?P<user_id>\d+)/$', views.index, name='index'),
    url(r'^', views.index, name='index'),
    url(r'^thankyou/', views.thankyou, name='thankyou'),
)
