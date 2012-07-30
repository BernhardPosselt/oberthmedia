#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Django imports
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

# generate top url for appending to urls
project_url = ''
if len(settings.PROJECT_URL) > 1:
    project_url = settings.PROJECT_URL[1:] + '/'

urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^' + project_url, include('oberthmedia.homepage.urls', namespace='homepage', app_name='homepage')),
)
