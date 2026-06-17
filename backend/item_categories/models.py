from django.db import models


class Categories(models.Model):
    name = models.CharField(null=False, blank=False)
    eng_name = models.CharField(null=False, blank=False)

    def __str__(self):
        return self.name