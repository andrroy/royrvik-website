from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', views.notes),
    url(r'^(?P<post_id>\d+)/$', views.post),
    url(r'^search/(?P<username>\w{0,50})/$', views.user_posts),
    url(r'^search/(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})/$', views.date_posts),
)