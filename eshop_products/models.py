from django.db import models

from eshop_products_category.models import category
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db.models import Q


# Create your models here.

class ProductManager(models.Manager):
    def active_check(self):
        active = self.get_queryset().filter(active=True)
        return active

    def get_by_slug_id(self, slug, id):
        Slug = self.get_queryset().filter(slug=slug, id=id)
        if not Slug.exists():
            return None
        return Slug.first()

    def search_and_price(self, qs, min_price, max_price):
        lookup = Q(title__icontains=qs) | Q(description__icontains=qs) | Q(tag__title__icontains=qs)
        products = self.get_queryset().filter(lookup, active=True,price__range = (min_price,max_price),free=False).distinct()

        if products is None:
            return None
        else:
            return products

    def search(self, qs):
        lookup = Q(title__icontains=qs) | Q(description__icontains=qs) | Q(tag__title__icontains=qs)

        products = self.get_queryset().filter(lookup, active=True).distinct()

        if products is None:
            return None
        else:
            return products

    # def related_products(self ,category):
    #     related = self.get_queryset().filter(categories__product=category)
    #     return related


class Product(models.Model):
    title = models.CharField(max_length=45, verbose_name="عنوان")
    description = models.TextField(default='none', verbose_name='توضیحات')
    price = models.IntegerField(default='0', verbose_name='قیمت')
    image = models.ImageField(upload_to='products/',null=True,blank=True)
    active = models.BooleanField(default=False, verbose_name='وضعیت')
    free = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)
    categories = models.ManyToManyField(category, null=True, blank=True)
    views = models.IntegerField(default=0) 
    teacher = models.CharField(default="مشخص نشده!!!",max_length=50)
    objects = ProductManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "محصولات"
        verbose_name_plural = "محصول"


def pre_save_slug_rec(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_slug_rec, sender=Product)


class Product_gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='product_gallery/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "گالری ها"
        verbose_name_plural = "گالری محصولات"
