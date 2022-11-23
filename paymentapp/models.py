from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=255)
    discription = models.TextField(blank=True, null=True)
    price = models.IntegerField()
