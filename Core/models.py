import os
import shutil
from django.conf import settings
from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io
from django.utils.translation import gettext_lazy as _


class FAQ(DateMixin):
    faq = models.CharField(_('faq'), max_length=300, unique=True)
    answer = models.CharField(_('answer'), max_length=300)
    is_active = models.BooleanField(_('is_active'), default=True)

    def __str__(self):
        return self.faq

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQ')


class Subscribe(DateMixin):
    email = models.EmailField(_('email'), max_length=50, unique=True)
    is_active = models.BooleanField(_('is_active'), default=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Subscribe')
        verbose_name_plural = _('Subscribe')


class Partner(DateMixin):
    partner_name = models.CharField(_('partner_name'), max_length=255, unique=True)
    original_partner_logo = models.ImageField(_('original_partner_logo'), upload_to=Uploader.partner_logo_original, max_length=255)
    compress_partner_logo = models.ImageField(_('compress_partner_logo'), upload_to=Uploader.partner_logo_compress, max_length=255, null=True, blank=True)
    is_active = models.BooleanField(_('is_active'), default=True)

    def __str__(self):
        return self.partner_name

    def save(self, *args, **kwargs):

        if self.original_partner_logo:
            img = Image.open(self.original_partner_logo)

            if img.mode == 'RGBA':
                img = img.convert('RGB')

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=60)
            img_io.seek(0)

            self.compress_partner_logo = SimpleUploadedFile(
                name=self.original_partner_logo.name,
                content=img_io.getvalue(),
                content_type='image/jpeg'
            )

        if self.pk:

            old_instance = Partner.objects.get(pk=self.pk)

            # Check if the original_blog_image has been changed
            if self.original_partner_logo != old_instance.original_partner_logo:
                if old_instance.original_partner_logo:
                    # Delete original image
                    if os.path.isfile(old_instance.original_partner_logo.path):
                        os.remove(old_instance.original_partner_logo.path)
                    # Delete compressed image
                    if old_instance.compress_partner_logo and os.path.isfile(old_instance.compress_partner_logo.path):
                        os.remove(old_instance.compress_partner_logo.path)

            # Check if the original_blog_image has been cleared
            if not self.original_partner_logo:
                # Delete old images if they exist
                if old_instance.original_partner_logo:
                    self.compress_partner_logo = None
                    # Delete original image
                    if os.path.isfile(old_instance.original_partner_logo.path):
                        os.remove(old_instance.original_partner_logo.path)
                    # Delete compressed image
                    if old_instance.compress_partner_logo and os.path.isfile(old_instance.compress_partner_logo.path):
                        os.remove(old_instance.compress_partner_logo.path)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Get the paths to the original and compressed blog folders
        original_blog_category_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Partner', self.partner_name)
        compress_blog_category_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Partner', self.partner_name)

        # Delete the original blog folder and its contents
        if os.path.exists(original_blog_category_folder):
            shutil.rmtree(original_blog_category_folder)

        # Delete the compressed blog folder and its contents
        if os.path.exists(compress_blog_category_folder):
            shutil.rmtree(compress_blog_category_folder)

        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partner')
