from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from home.views import home


from django.views.generic import TemplateView
urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
    url(r'^notes/', include('notes.urls'), name='notes'),
    
    url(r'^transfers/', include('transfers.urls'), name='transfers'),
    url(r'^hwreader/', 'hwreader.views.home', name='hwreader'),
    
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^login/$', login, {'template_name': '../templates/auth/login.html'}),
    url(r'^logout/$', logout, {'next_page': '/'}),
    
    #Deactivated/Not in use
    #url(r'^vb/', 'vb.views.home', name='vb'),
    #url(r'^profile/$', TemplateView.as_view(template_name='/Users/andrroy/Documents/git/new-website/pwebsite/templates/registration/profile.html')),
    #url(r'^vb/', include('vb.urls'), name='vb'),
    #url(r'^fitness/', 'fitness.views.home', name='fitness'),
)

handler404 = 'pwebsite.views.handler404'
