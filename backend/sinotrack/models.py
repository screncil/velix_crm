from django.db import models
from datetime import timedelta

# Create your models here.


class Sinotrack(models.Model):
    _id = models.CharField(blank=False, null=False)
    phone_number = models.CharField(blank=False, null=False)
    payment_date = models.DateField(blank=False, null=False)
    end_date_rate = models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.payment_date:
            self.end_date_rate = self.payment_date + timedelta(days=84)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self._id} | {self.phone_number}"