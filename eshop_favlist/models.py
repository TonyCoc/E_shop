from django.contrib.auth.models import User
from django.db import models
from eshop_products.models import Product


class Favorite_list(models.Model):

    user = models.OneToOneField(User, models.CASCADE)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "لیست کابر"
        verbose_name_plural = "لیست های کاربران"


class details(models.Model):
    favorite_list = models.ForeignKey(Favorite_list, models.CASCADE)

    product = models.ForeignKey(Product, models.CASCADE)



    def __str__(self):
        return self.favorite_list.user.username

    class Meta:
        verbose_name = "محصول درون لیست"
        verbose_name_plural = "محصولات درون لیست"
