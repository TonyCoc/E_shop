from django.contrib.auth.models import User
from django.db import models

from eshop_products.models import Product


class order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    add_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.owner.get_username()

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = "سبد های خرید"


class order_detail(models.Model):
    order = models.ForeignKey(order, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()

    def total_price(self):
       return self.price * self.count

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = "جزییات خرید"
        verbose_name_plural = "جزییات خرید ها"
