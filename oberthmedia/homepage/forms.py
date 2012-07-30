#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django import forms
#from django.utils.translation import ugettext_lazy as _

from oberthmedia.homepage.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact


#from oberthmedia.defaultpapp.models import UserProfile

#class UserProfileForm(forms.ModelForm):
#    class Meta:
#        model: UserProfile
