import os
import io
import shutil
from django.conf import settings
from django.db import models
from Service.models import Service
from services.mixins import DateMixin
from django.utils.crypto import get_random_string
from django.template.defaultfilters import slugify
from services.uploader import Uploader
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
from django.utils.translation import gettext_lazy as _
from modeltranslation.utils import build_localized_fieldname



class Project(DateMixin):
    project_title = models.CharField(_('project_title'), max_length=255)
    project_slug = models.SlugField(_('project_slug'), null=True, blank=True, unique=True)
    project_original_image = models.ImageField(_('project_original_image'), upload_to=Uploader.project_image_original, max_length=255)
    project_compress_image = models.ImageField(_('project_compress_image'), upload_to=Uploader.project_image_compress, max_length=255, null=True, blank=True)
    project_link = models.URLField(_('project_link'), max_length=255, null=True, blank=True)
    project_is_show = models.BooleanField(_('project_is_show'), default=True)
    service = models.ForeignKey(Service, verbose_name=_('service'), on_delete=models.CASCADE, related_name='related_service_project')

    def __str__(self):
        return self.project_title

    def save(self, *args, **kwargs):

        # Compress the image if it exists
        if self.project_original_image:

            img = Image.open(self.project_original_image)

            # Convert image to RGB mode if it's in RGBA mode
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=60)
            img_io.seek(0)

            # Save the compressed image to project_compress_image field
            self.project_compress_image = SimpleUploadedFile(
                name=self.project_original_image.name,
                content=img_io.getvalue(),
                content_type='image/jpeg'
            )

        if self.pk:
            # Retrieve the existing instance from the database
            old_instance = Project.objects.get(pk=self.pk)

            # Check if the project_original_image has been changed
            if self.project_original_image != old_instance.project_original_image:
                # Delete old images if they exist
                if old_instance.project_original_image:
                    # Delete original image
                    if os.path.isfile(old_instance.project_original_image.path):
                        os.remove(old_instance.project_original_image.path)
                    # Delete compressed image
                    if old_instance.project_compress_image and os.path.isfile(old_instance.project_compress_image.path):
                        os.remove(old_instance.project_compress_image.path)

            # Check if the project_original_image has been cleared
            if not self.project_original_image:
                # Delete old images if they exist
                if old_instance.project_original_image:
                    self.project_compress_image = None
                    # Delete original image
                    if os.path.isfile(old_instance.project_original_image.path):
                        os.remove(old_instance.project_original_image.path)
                    # Delete compressed image
                    if old_instance.project_compress_image and os.path.isfile(old_instance.project_compress_image.path):
                        os.remove(old_instance.project_compress_image.path)

        # Generate and save the slug for the default language
        if not self.project_slug:
            self.project_slug = slugify(self.project_title)

            # Ensure uniqueness of the slug
            suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
            while Project.objects.filter(project_slug=self.project_slug + suffix).exclude(pk=self.pk).exists():
                suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
            self.project_slug = f"{self.project_slug}-{suffix}"

        # Generate and save the slugs for other languages
        for lang_code, _ in settings.LANGUAGES:
            if lang_code != settings.LANGUAGE_CODE:
                title_field = build_localized_fieldname('project_title', lang_code)
                if hasattr(self, title_field) and not getattr(self, f'project_slug_{lang_code}'):
                    title_value = getattr(self, title_field)
                    if title_value:
                        project_slug = slugify(title_value)

                        # Ensure uniqueness of the slug
                        suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
                        while Project.objects.filter(**{f'project_slug_{lang_code}': project_slug + suffix}).exclude(pk=self.pk).exists():
                            suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
                        setattr(self, f'project_slug_{lang_code}', f"{project_slug}-{suffix}")

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        original_project_folder = os.path.join(settings.MEDIA_ROOT, 'Original-Image', 'Service', self.service.service_title, 'Project-Image', self.project_title)
        compress_project_folder = os.path.join(settings.MEDIA_ROOT, 'Compress-Image', 'Service', self.service.service_title, 'Project-Image', self.project_title)

        # Delete the original service folder and its contents
        if os.path.exists(original_project_folder):
            shutil.rmtree(original_project_folder)

        # Delete the compressed service folder and its contents
        if os.path.exists(compress_project_folder):
            shutil.rmtree(compress_project_folder)

        # Call the delete method of the parent class
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Project')


class ProjectAllImage(DateMixin):
    original_image = models.ImageField(_('original_image'), upload_to=Uploader.project_all_images_original, max_length=255)
    compress_image = models.ImageField(_('compress_image'), upload_to=Uploader.project_all_images_compress, max_length=255, null=True, blank=True)
    image_is_show = models.BooleanField(_('image_is_show'), default=True)
    project = models.ForeignKey(Project, verbose_name=_('project'), on_delete=models.CASCADE, related_name='related_image_project')

    def __str__(self):
        return f"{self.project.project_title} image {self.pk}"

    def save(self, *args, **kwargs):
        # Compress the image if it exists
        if self.original_image:
            img = Image.open(self.original_image)

            # Convert image to RGB mode if it's in RGBA mode
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=60)
            img_io.seek(0)

            # Save the compressed image to compress_image field
            self.compress_image = SimpleUploadedFile(
                name=self.original_image.name,
                content=img_io.getvalue(),
                content_type='image/jpeg'
            )

        if self.pk:
            # Retrieve the existing instance from the database
            old_instance = ProjectAllImage.objects.get(pk=self.pk)

            # Check if the original_image has been changed
            if self.original_image != old_instance.original_image:
                # Delete old images if they exist
                if old_instance.original_image:
                    # Delete original image
                    if os.path.isfile(old_instance.original_image.path):
                        os.remove(old_instance.original_image.path)
                    # Delete compressed image
                    if old_instance.compress_image and os.path.isfile(old_instance.compress_image.path):
                        os.remove(old_instance.compress_image.path)

            # Check if the original_image has been cleared
            if not self.original_image:
                # Delete old images if they exist
                if old_instance.original_image:
                    self.compress_image = None
                    # Delete original image
                    if os.path.isfile(old_instance.original_image.path):
                        os.remove(old_instance.original_image.path)
                    # Delete compressed image
                    if old_instance.compress_image and os.path.isfile(old_instance.compress_image.path):
                        os.remove(old_instance.compress_image.path)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the images associated with the blog instance
        if self.original_image:
            storage, path = self.original_image.storage, self.original_image.path
            storage.delete(path)

        if self.compress_image:
            storage, path = self.compress_image.storage, self.compress_image.path
            storage.delete(path)

        # Call the delete method of the parent class
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Project All Image')
        verbose_name_plural = _('Project All Image')
