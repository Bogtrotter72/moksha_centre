from django.db import models
from taggit.managers import TaggableManager


class Product(models.Model):
    sku = models.CharField(max_length = 254)
    manufacturer = models.CharField(max_length = 254)
    name = models.CharField(max_length = 254)
    description = models.TextField()
    color = models.CharField(max_length=254, null=True, blank=True)
    dimensions = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = TaggableManager()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name