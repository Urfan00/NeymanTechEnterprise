from django.db import models
from services.mixins import DateMixin
from django.utils.translation import gettext_lazy as _


class WebsiteRequest(DateMixin):
    fullname = models.CharField(_('fullname'), max_length=50)
    phone_number = models.CharField(_('phone_number'), max_length=20)
    request = models.TextField(_('request'), )
    company = models.CharField(_('company'), max_length=255, null=True, blank=True)
    is_view = models.BooleanField(_('is_view'), default=False)
    admin_comment = models.CharField(_('admin_comment'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = _('Website Request')
        verbose_name_plural = _('Website Request')
