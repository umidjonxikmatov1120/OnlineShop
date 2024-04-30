from django.db import models


class ProductsModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.name