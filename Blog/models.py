import os
import io
from PIL import Image
from django.db import models
from services.mixins import DateMixin
from ckeditor.fields import RichTextField
from django.utils.crypto import get_random_string
from django.template.defaultfilters import slugify
from services.uploader import Uploader
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.translation import gettext_lazy as _
from modeltranslation.utils import build_localized_fieldname
from django.conf import settings



class BlogCategory(DateMixin):
    blog_category_title = models.CharField(_('blog_category_title'), max_length=50)
    is_active = models.BooleanField(_('is_active'), default=True)

    def delete(self, *args, **kwargs):
        # Delete related blog images
        for blog in self.related_blog_category.all():
            if blog.original_blog_image:
                storage, path = blog.original_blog_image.storage, blog.original_blog_image.path
                storage.delete(path)
                folder_path = os.path.dirname(path)
                os.rmdir(folder_path)  # Delete the folder

            if blog.compress_blog_image:
                storage, path = blog.compress_blog_image.storage, blog.compress_blog_image.path
                storage.delete(path)
                folder_path = os.path.dirname(path)
                os.rmdir(folder_path)  # Delete the folder

        # Call the delete method of the parent class
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.blog_category_title

    class Meta:
        verbose_name = _('Blog Category')
        verbose_name_plural = _('Blog Category')


class Blog(DateMixin):
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), null=True, blank=True, unique=True)
    show_date = models.DateField(_('show_date'), )
    content = RichTextField(_('content'), )
    is_show = models.BooleanField(_('is_show'), default=True)
    original_blog_image = models.ImageField(_('original_blog_image'), upload_to=Uploader.blog_images_original, max_length=255)
    compress_blog_image = models.ImageField(_('compress_blog_image'), upload_to=Uploader.blog_images_compress, max_length=255, null=True, blank=True)
    blog_category = models.ForeignKey(BlogCategory, verbose_name=_('blog_category'), on_delete=models.CASCADE, related_name='related_blog_category')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        # Compress the image if it exists
        if self.original_blog_image:

            img = Image.open(self.original_blog_image)

            # Convert image to RGB mode if it's in RGBA mode
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            img_io = io.BytesIO()
            img.save(img_io, format='JPEG', quality=60)
            img_io.seek(0)

            # Save the compressed image to compress_blog_image field
            self.compress_blog_image = SimpleUploadedFile(
                name=self.original_blog_image.name,
                content=img_io.getvalue(),
                content_type='image/jpeg'
            )

        if self.pk:
            # Retrieve the existing instance from the database
            old_instance = Blog.objects.get(pk=self.pk)

            # Check if the original_blog_image has been changed
            if self.original_blog_image != old_instance.original_blog_image:
                # Delete old images if they exist
                if old_instance.original_blog_image:
                    # Delete original image
                    if os.path.isfile(old_instance.original_blog_image.path):
                        os.remove(old_instance.original_blog_image.path)
                    # Delete compressed image
                    if old_instance.compress_blog_image and os.path.isfile(old_instance.compress_blog_image.path):
                        os.remove(old_instance.compress_blog_image.path)

            # Check if the original_blog_image has been cleared
            if not self.original_blog_image:
                # Delete old images if they exist
                if old_instance.original_blog_image:
                    self.compress_blog_image = None
                    # Delete original image
                    if os.path.isfile(old_instance.original_blog_image.path):
                        os.remove(old_instance.original_blog_image.path)
                    # Delete compressed image
                    if old_instance.compress_blog_image and os.path.isfile(old_instance.compress_blog_image.path):
                        os.remove(old_instance.compress_blog_image.path)

        # Generate and save the slug for the default language
        if not self.slug:
            self.slug = slugify(self.title)

            # Ensure uniqueness of the slug
            suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
            while Blog.objects.filter(slug=self.slug + suffix).exclude(pk=self.pk).exists():
                suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
            self.slug = f"{self.slug}-{suffix}"

        # Generate and save the slugs for other languages
        for lang_code, _ in settings.LANGUAGES:
            if lang_code != settings.LANGUAGE_CODE:
                title_field = build_localized_fieldname('title', lang_code)
                if hasattr(self, title_field) and not getattr(self, f'slug_{lang_code}'):
                    title_value = getattr(self, title_field)
                    if title_value:
                        slug = slugify(title_value)

                        # Ensure uniqueness of the slug
                        suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
                        while Blog.objects.filter(**{f'slug_{lang_code}': slug + suffix}).exclude(pk=self.pk).exists():
                            suffix = get_random_string(length=4, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyz')
                        setattr(self, f'slug_{lang_code}', f"{slug}-{suffix}")

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the images associated with the blog instance
        if self.original_blog_image:
            storage, path = self.original_blog_image.storage, self.original_blog_image.path
            storage.delete(path)
            folder_path = os.path.dirname(path)
            os.rmdir(folder_path)  # Delete the folder

        if self.compress_blog_image:
            storage, path = self.compress_blog_image.storage, self.compress_blog_image.path
            storage.delete(path)
            folder_path = os.path.dirname(path)
            os.rmdir(folder_path)  # Delete the folder

        # Call the delete method of the parent class
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blog')
