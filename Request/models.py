from django.db import models
from services.mixins import DateMixin


class WebsiteRequest(DateMixin):
    fullname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    request = models.TextField()
    company = models.CharField(max_length=255, null=True, blank=True)
    is_view = models.BooleanField(default=False)
    admin_comment = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Website Request'
        verbose_name_plural = 'Website Request'
