from django.db import models
from services.mixins import DateMixin


class CostumerReview(DateMixin):
    fullname = models.CharField(max_length=50)
    costumer_company = models.CharField(max_length=255, null=True, blank=True)
    costumer_review = models.CharField(max_length=255)
    is_show = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Costumer Review'
        verbose_name_plural = 'Costumer Review'
