#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Django imports
from django.conf.urls.defaults import *

# main views
urlpatterns = patterns('oberthmedia.homepage.views.main',
    url(r'^$', 'index', name='index'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^agb/$', 'agb', name='agb'),
    url(r'^impressum/$', 'sitenotice', name='sitenotice'),
    url(r'^js/settings/', 'js_settings', name='js_settings'),
    #url(r'^logout/', 'logout_to_index', name='logout_to_index'),
)

#urlpatterns += patterns('django.contrib.auth.views',
#    url(r'^login/$', 'login', {'template_name': 'homepage/login.html'}, name='login'),
#)
