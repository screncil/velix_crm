from django.db import models
from sinotrack.models import Sinotrack

# Create your models here.

class Bike(models.Model):
    _id = models.CharField(null=False, blank=False)
    name = models.CharField(null=False, blank=False)
    model = models.CharField(null=False, blank=False)
    serial_number = models.CharField(null=False, blank=False)
    wheel_diameter = models.IntegerField(null=False, blank=False)
    rental_price = models.FloatField(null=False, blank=False)
    additional_rental_price = models.FloatField(null=False, blank=False, default=0)
    comments = models.CharField()
    pledge = models.FloatField(null=False, blank=False)
    sinotrack = models.ForeignKey(Sinotrack, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.model} {self.serial_number}"