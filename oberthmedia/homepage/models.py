#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

#class UserProfile(models.Model):
#    user = models.OneToOneField("auth.User")


class Contact(models.Model):
    name = models.CharField(_(u"Name"), max_length=200, help_text=_(u"Wie heißen \
        Sie und/oder Ihre Firma?"))
    phone = models.CharField(_(u"Telefon"), max_length=200, blank=True,
        help_text=_(u"Unter welcher Telefon-Nummer..."))
    phonetime = models.CharField(_(u"Anruf möglich um"), max_length=200,
        blank=True, help_text=_(u"Wann wollen Sie angerufen werden?"))
    email = models.EmailField(_(u"E-Mail"), max_length=200, help_text=_("...\
        oder welcher E-Mail Adresse dürfen wir Ihnen antworten?"))
    message = models.TextField(_(u"Nachricht"), help_text=_(u"Was haben Sie für \
        Wünsche?"))
    timestamp = models.DateTimeField(_(u"Sendedatum"), auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u"Kontaktanfrage")
        verbose_name_plural = _(u"Kontaktanfragen")
        ordering = ['-timestamp']


class Reference(models.Model):
    title = models.CharField(_(u"Titel"), max_length=200)
    description = models.TextField(_(u"Kurzbeschreibung"),
        help_text=_(u"Zusammenfassender Einleitungstext, der über der Gallerie \
            angezeigt wird"))
    cover = models.ImageField(_(u"Vorschaubild"), help_text=_(u"Das kleine Bild, \
        welches in der Übersicht auftaucht (334px breit, 360px hoch)"), upload_to="references")
    timestamp = models.DateTimeField(_(u"Erstelldatum"), auto_now_add=True)
    active = models.BooleanField(_(u"Öffentlich"), help_text=_(u"Wenn gesetzt \
        erscheint der Eintrag in der Referenzgallerie"), default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _(u"Referenz")
        verbose_name_plural = _(u"Referenzen")
        ordering = ['-timestamp']
