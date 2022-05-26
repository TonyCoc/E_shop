from django.db import models
from django.db.models.signals import pre_save, post_save

from eshop_products.models import Product
from .utils import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=150,verbose_name="عنوان")
    slug = models.SlugField(blank=True,verbose_name="عنوان در یو ار ال")
    time = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product,verbose_name="محصولات مربوطه")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "برچسب ها"
        verbose_name_plural = "برچسب"


def pre_save_tag_rec(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_tag_rec, sender=Tag)

