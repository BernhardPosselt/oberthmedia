#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

#class UserProfile(models.Model):
#    user = models.OneToOneField("auth.User")


class Contact(models.Model):
    name = models.CharField(_("Name"), max_length=200, help_text=_("Wie heißen \
        Sie und/oder Ihre Firma?"))
    phone = models.CharField(_("Telefon"), max_length=200, blank=True,
        help_text=_("Unter welcher Telefon-Nummer..."))
    phonetime = models.CharField(_("Anruf möglich um"), max_length=200,
        blank=True, help_text=_("Wann wollen Sie angerufen werden?"))
    email = models.EmailField(_("E-Mail"), max_length=200, help_text=_("...\
        oder welcher E-Mail Adresse dürfen wir Ihnen antworten?"))
    message = models.TextField(_("Nachricht"), help_text=_("Was haben Sie für \
        Wünsche?"))
    timestamp = models.DateTimeField(_("Sendedatum"), auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("Kontaktanfrage")
        verbose_name_plural = _("Kontaktanfragen")
        ordering = ['-timestamp']


class Reference(models.Model):
    title = models.CharField(_("Titel"), max_length=200)
    description = models.TextField(_("Kurzbeschreibung"),
        help_text=_("Zusammenfassender Einleitungstext, der über der Gallerie \
            angezeigt wird"))
    cover = models.ImageField(_("Vorschaubild"), help_text=_("Das kleine Bild, \
        welches in der Übersicht auftaucht"), upload_to="references")
    timestamp = models.DateTimeField(_("Erstelldatum"), auto_now_add=True)
    active = models.BooleanField(_("Öffentlich"), help_text=_("Wenn gesetzt \
        erscheint der Eintrag in der Referenzgallerie"), default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("Referenz")
        verbose_name_plural = _("Referenzen")
        ordering = ['-timestamp']
