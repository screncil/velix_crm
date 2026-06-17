from django.db import models
from sinotrack.models import Sinotrack

# Create your models here.

class Bike(models.Model):
    name = models.CharField(null=False, blank=False)
    model = models.CharField(null=False, blank=False)
    serial_number = models.CharField(null=False, blank=False)
    wheel_diameter = models.FloatField(null=False, blank=False)
    comments = models.CharField()
    in_rent = models.BooleanField(null=False, blank=False, default=False)
    sinotrack = models.ForeignKey(Sinotrack, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} {self.model} {self.serial_number}"