from django.db import models

class RequestRecord(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)

    