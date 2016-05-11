from __future__ import unicode_literals

from django.db import models


class Suscriptor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=240)
