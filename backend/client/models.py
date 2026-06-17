from django.db import models


class WhereKnow(models.Model):
    name = models.CharField(null=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    fio = models.CharField(null=False, blank=False)
    phone_number = models.CharField(null=False, blank=False)
    comment = models.CharField(default="", null=True, blank=True)
    where_know = models.ForeignKey(WhereKnow, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.fio

