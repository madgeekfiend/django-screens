from django.conf.urls import patterns, url
from website import views

urlpatterns = patterns('',
    # You know what this file is for


    url(r'^upload/', views.upload, name='upload'),
    url(r'^review/', views.review, name='review'),
    url(r'^(?P<screen_id>\d+)/$', views.view_screen, name='view_screen'),
    url(r'^(?P<screen_id>\d+)/comment/$', views.comment, name='comment'),
)
