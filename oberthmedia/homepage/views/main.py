#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from oberthmedia.homepage.forms import ContactForm
from oberthmedia.homepage.models import Reference


def index(request):
    refs = Reference.objects.filter(active=True)
    leftToGenerate = range(3 - (len(refs) % 3))
    ctx = {
        "active_tab": "index",
        "references": refs,
        "generate_bulks": leftToGenerate
    }
    return render(request, 'homepage/index.html', ctx)


def reference(request, refId):
    ref = get_object_or_404(Reference, pk=refId)
    ctx = {
        "active_tab": "index",
        "ref": ref
    }
    return render(request, 'homepage/reference.html', ctx)


def about(request):
    ctx = {
        "active_tab": "about"
    }
    return render(request, 'homepage/about.html', ctx)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('homepage:contact_success'))
    else:
        form = ContactForm()
    ctx = {
        'contact_form': form,
        "active_tab": "contact"
    }
    return render(request, 'homepage/contact.html', ctx)


def contact_success(request):
    ctx = {
        "active_tab": "contact"
    }
    return render(request, 'homepage/contact_success.html', ctx)


def agb(request):
    ctx = {
        "active_tab": "agb"
    }
    return render(request, 'homepage/agb.html', ctx)


def sitenotice(request):
    ctx = {
        "active_tab": "sitenotice"
    }
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
