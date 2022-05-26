from django.contrib.auth.models import User
from django.db import models
from eshop_products.models import Product


class CommentModel(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=700)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True , blank=True , null=True)

    def __str__(self):
        return self.person.get_username()

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
