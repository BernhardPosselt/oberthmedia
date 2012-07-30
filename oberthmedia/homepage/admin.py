#!/usr/bin/env python
#-*- coding:utf-8 -*-

from oberthmedia.homepage.models import Contact, Reference
from django.contrib import admin


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'timestamp', 'message']
    ordering = ['-timestamp']
    search_fields = ['name', 'email', 'message', 'phone']
    list_filter = ['email', 'timestamp']
    date_hierarchy = 'timestamp'


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'active', 'timestamp']
    ordering = ['-timestamp']
    search_fields = ['title', 'description', 'active', 'timestamp']
    list_filter = ['timestamp', 'active']
    date_hierarchy = 'timestamp'


admin.site.register(Contact, ContactAdmin)
admin.site.register(Reference, ReferenceAdmin)
