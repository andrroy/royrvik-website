from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^sumo/$', views.sumo),
    url(r'^itk-ro/$', views.itk_ro),
    url(r'^info-screen/$', views.info_screen),
    )