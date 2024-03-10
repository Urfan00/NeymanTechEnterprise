from django.db import models
from services.mixins import DateMixin
from django.utils.translation import gettext_lazy as _


class CostumerReview(DateMixin):
    fullname = models.CharField(_('fullname'), max_length=50)
    costumer_company = models.CharField(_('costumer_company'), max_length=255, null=True, blank=True)
    costumer_review = models.CharField(_('costumer_review'), max_length=255)
    is_show = models.BooleanField(_('is_show'), default=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = _('Costumer Review')
        verbose_name_plural = _('Costumer Review')
