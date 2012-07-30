#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json

from django.shortcuts import render  # ,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from oberthmedia.homepage.forms import ContactForm


def index(request):
    ctx = {
        "active_tab": "index"
    }
    return render(request, 'homepage/index.html', ctx)


def about(request):
    ctx = {
        "active_tab": "about"
    }
    return render(request, 'homepage/about.html', ctx)


def references(request, id):
    ctx = {
        "active_tab": "index"
    }
    return render(request, 'homepage/references.html', ctx)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('homepage:contact'))
    else:
        form = ContactForm()
    ctx = {
        'form': form,
        "active_tab": "contact"
    }
    return render(request, 'homepage/contact.html', ctx)


def agb(request):
    ctx = {
        "active_tab": "index"
    }
    return render(request, 'homepage/agb.html', ctx)


def sitenotice(request):
    ctx = {}
    return render(request, 'homepage/sitenotice.html', ctx)


def js_settings(request):
    settings = {
        #'homepage_index_url': reverse('homepage:index'),
    }
    return HttpResponse(json.dumps(settings), mimetype='application/json')


@login_required
def logout_to_index(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage:index'))
