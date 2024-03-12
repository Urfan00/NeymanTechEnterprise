from django.db import models
from services.mixins import DateMixin
from django.utils.translation import gettext_lazy as _



class DifferentUs(DateMixin):
    title = models.CharField(_('title'), max_length=255)
    content = models.TextField(_('content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Different Us')
        verbose_name_plural = _('Different Us')


class PhoneNumber(DateMixin):
    phone = models.CharField(_('phone'), max_length=12)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _('Phone Number')
        verbose_name_plural = _('Phone Number')


class EmailAddress(DateMixin):
    email = models.EmailField(_('email'), max_length=50)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Email Address')
        verbose_name_plural = _('Email Address')


class ContactInfo(DateMixin):
    phone = models.ManyToManyField(PhoneNumber, verbose_name=_('phone'), blank=True)
    email = models.ManyToManyField(EmailAddress, verbose_name=_('email'), blank=True)

    location_name = models.CharField(_('location_name'), max_length=255)
    location_url = models.URLField(_('location_url'), max_length=200)

    facebook = models.URLField(_('facebook'), max_length=200, null=True, blank=True)
    twitter = models.URLField(_('twitter'), max_length=200, null=True, blank=True)
    instagram = models.URLField(_('instagram'), max_length=200, null=True, blank=True)
    linkedln = models.URLField(_('linkedln'), max_length=200, null=True, blank=True)
    youtube = models.URLField(_('youtube'), max_length=200, null=True, blank=True)
    github = models.URLField(_('github'), max_length=200, null=True, blank=True)
    tiktok = models.URLField(_('tiktok'), max_length=200, null=True, blank=True)
    whatsapp = models.CharField(_('whatsapp'), max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = _('Contact Info')
        verbose_name_plural = _('Contact Info')
