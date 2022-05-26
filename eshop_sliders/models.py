from django.db import models

from eshop_products.models import Product


class Slider(models.Model):
    product = models.OneToOneField(Product ,on_delete=models.CASCADE )

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'اسلایدر ها'
        verbose_name_plural = "اسلایدر"