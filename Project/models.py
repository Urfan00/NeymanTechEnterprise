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



class Project(DateMixin):
    project_title = models.CharField(max_length=255)
    project_slug = models.SlugField(null=True, blank=True, unique=True)
    project_original_image = models.ImageField(upload_to=Uploader.project_image_original, max_length=255)
    project_compress_image = models.ImageField(upload_to=Uploader.project_image_compress, max_length=255, null=True, blank=True)
    project_link = models.URLField(max_length=255, null=True, blank=True)
    project_is_show = models.BooleanField(default=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='related_service_project')

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

        self.project_slug = slugify(self.project_title)

        while Project.objects.filter(project_slug=self.project_slug).exclude(pk=self.pk).exists():
            # Generate a unique slug by adding a suffix
            suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
            self.project_slug = f"{self.project_slug}-{suffix}"
        
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
        verbose_name = 'Project'
        verbose_name_plural = 'Project'


class ProjectAllImage(DateMixin):
    original_image = models.ImageField(upload_to=Uploader.project_all_images_original, max_length=255)
    compress_image = models.ImageField(upload_to=Uploader.project_all_images_compress, max_length=255, null=True, blank=True)
    image_is_show = models.BooleanField(default=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='related_image_project')

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
        verbose_name = 'Project All Image'
        verbose_name_plural = 'Project All Image'
