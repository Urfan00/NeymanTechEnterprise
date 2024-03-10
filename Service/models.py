import os
import io
import shutil
from django.conf import settings
from django.db import models
from services.mixins import DateMixin
from services.uploader import Uploader
from django.utils.crypto import get_random_string
from django.template.defaultfilters import slugify
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from django.utils.translation import gettext_lazy as _


class Service(DateMixin):
    service_title = models.CharField(_('service_title'), max_length=255)
    service_slug = models.SlugField(_('service_slug'), null=True, blank=True, unique=True)
    service_original_icon = models.ImageField(_('service_original_icon'), upload_to=Uploader.service_icon_original, max_length=255)
    service_compress_icon = models.ImageField(_('service_compress_icon'), upload_to=Uploader.service_icon_compress, max_length=255, null=True, blank=True)
    description = models.TextField(_('description'), )
    service_is_show = models.BooleanField(_('service_is_show'), default=True)

    def __str__(self):
        return self.service_title

    def save(self, *args, **kwargs):

        # Compress the image if it exists
        if self.service_original_icon:

            img = Image.open(self.service_original_icon)

            # Convert image to RGB mode if it's in RGBA mode
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=60)
            img_io.seek(0)

            # Save the compressed image to service_compress_icon field
            self.service_compress_icon = SimpleUploadedFile(
                name=self.service_original_icon.name,
                content=img_io.getvalue(),
                content_type='image/jpeg'
            )

        if self.pk:
            # Retrieve the existing instance from the database
            old_instance = Service.objects.get(pk=self.pk)

            # Check if the service_original_icon has been changed
            if self.service_original_icon != old_instance.service_original_icon:
                # Delete old images if they exist
                if old_instance.service_original_icon:
                    # Delete original image
                    if os.path.isfile(old_instance.service_original_icon.path):
                        os.remove(old_instance.service_original_icon.path)
                    # Delete compressed image
                    if old_instance.service_compress_icon and os.path.isfile(old_instance.service_compress_icon.path):
                        os.remove(old_instance.service_compress_icon.path)

            # Check if the service_original_icon has been cleared
            if not self.service_original_icon:
                # Delete old images if they exist
                if old_instance.service_original_icon:
                    self.service_compress_icon = None
                    # Delete original image
                    if os.path.isfile(old_instance.service_original_icon.path):
                        os.remove(old_instance.service_original_icon.path)
                    # Delete compressed image
                    if old_instance.service_compress_icon and os.path.isfile(old_instance.service_compress_icon.path):
                        os.remove(old_instance.service_compress_icon.path)

        self.service_slug = slugify(self.service_title)

        while Service.objects.filter(service_slug=self.service_slug).exclude(pk=self.pk).exists():
            # Generate a unique slug by adding a suffix
            suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
            self.service_slug = f"{self.service_slug}-{suffix}"

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        # Get the paths to the original and compressed service folders
        original_service_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Service', self.service_title)
        compress_service_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Service', self.service_title)

        # Delete the original service folder and its contents
        if os.path.exists(original_service_folder):
            shutil.rmtree(original_service_folder)

        # Delete the compressed service folder and its contents
        if os.path.exists(compress_service_folder):
            shutil.rmtree(compress_service_folder)

        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Service')


class ServiceCard(DateMixin):
    service_card_title = models.CharField(_('service_card_title'), max_length=255)
    service_card_content = models.TextField(_('service_card_content'), )
    service_card_is_show = models.BooleanField(_('service_card_is_show'), default=True)
    service = models.ForeignKey(Service, verbose_name=_('service'), on_delete=models.CASCADE, related_name='related_service')

    def __str__(self):
        return self.service_card_title

    class Meta:
        verbose_name = _('Service Card')
        verbose_name_plural = _('Service Card')
