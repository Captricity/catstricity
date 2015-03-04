from django.db import models

class Cat(models.Model):
    name = models.TextField(blank=False, null=False)
    image = models.ImageField(blank=False, null=False)
