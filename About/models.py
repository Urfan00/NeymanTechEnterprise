from django.db import models
from services.mixins import DateMixin



class DifferentUs(DateMixin):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Different Us'
        verbose_name_plural = 'Different Us'


class PhoneNumber(DateMixin):
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Phone Number'
        verbose_name_plural = 'Phone Number'


class EmailAddress(DateMixin):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Email Address'
        verbose_name_plural = 'Email Address'


class ContactInfo(DateMixin):
    phone = models.ManyToManyField(PhoneNumber, blank=True)
    email = models.ManyToManyField(EmailAddress, blank=True)

    location_name = models.CharField(max_length=255)
    location_url = models.URLField(max_length=200)

    facebook = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    linkedln = models.URLField(max_length=200, null=True, blank=True)
    youtube = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    tiktok = models.URLField(max_length=200, null=True, blank=True)
    whatsapp = models.URLField(max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'
