import os
import io
import shutil
from django.conf import settings
from django.db import models
from services.mixins import DateMixin
from django.utils.translation import gettext_lazy as _
from services.uploader import Uploader
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image


class CostumerReview(DateMixin):
    fullname = models.CharField(_('fullname'), max_length=50)
    costumer_company = models.CharField(_('costumer_company'), max_length=255, null=True, blank=True)
    costumer_review = models.CharField(_('costumer_review'), max_length=255)
    is_show = models.BooleanField(_('is_show'), default=True)
    original_costumer_image = models.ImageField(_('original_costumer_image'), upload_to=Uploader.costumer_image_original, max_length=255)
    compress_costumer_image = models.ImageField(_('compress_costumer_image'), upload_to=Uploader.costumer_image_compress, max_length=255, null=True, blank=True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):

        # Compress the image if it exists
        if self.original_costumer_image:

            img = Image.open(self.original_costumer_image)

            # Convert image to RGB mode if it's in RGBA mode
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=60)
            img_io.seek(0)

            # Save the compressed image to compress_costumer_image field
            self.compress_costumer_image = SimpleUploadedFile(
                name=self.original_costumer_image.name,
                content=img_io.getvalue(),
                content_type='image/jpeg'
            )

        if self.pk:
            # Retrieve the existing instance from the database
            old_instance = CostumerReview.objects.get(pk=self.pk)

            # Check if the original_costumer_image has been changed
            if self.original_costumer_image != old_instance.original_costumer_image:
                # Delete old images if they exist
                if old_instance.original_costumer_image:
                    # Delete original image
                    if os.path.isfile(old_instance.original_costumer_image.path):
                        os.remove(old_instance.original_costumer_image.path)
                    # Delete compressed image
                    if old_instance.compress_costumer_image and os.path.isfile(old_instance.compress_costumer_image.path):
                        os.remove(old_instance.compress_costumer_image.path)

            # Check if the original_costumer_image has been cleared
            if not self.original_costumer_image:
                # Delete old images if they exist
                if old_instance.original_costumer_image:
                    self.compress_costumer_image = None
                    # Delete original image
                    if os.path.isfile(old_instance.original_costumer_image.path):
                        os.remove(old_instance.original_costumer_image.path)
                    # Delete compressed image
                    if old_instance.compress_costumer_image and os.path.isfile(old_instance.compress_costumer_image.path):
                        os.remove(old_instance.compress_costumer_image.path)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        original_costumer_image_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Costumer-Image', self.fullname)
        compress_costumer_image_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Costumer-Image', self.fullname)

        # Delete the original service folder and its contents
        if os.path.exists(original_costumer_image_folder):
            shutil.rmtree(original_costumer_image_folder)

        # Delete the compressed service folder and its contents
        if os.path.exists(compress_costumer_image_folder):
            shutil.rmtree(compress_costumer_image_folder)

        # Call the delete method of the parent class
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Costumer Review')
        verbose_name_plural = _('Costumer Review')
