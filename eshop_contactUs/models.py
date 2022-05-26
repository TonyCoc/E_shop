from django.core import validators
from django.db import models

# Create your models here.

class Contact_us_model(models.Model):
    full_name = models.CharField(max_length=150,verbose_name="نام و نام خانوادگی")
    email = models.EmailField(max_length=150,verbose_name="ایمیل")
    subject = models.CharField(max_length=200,verbose_name="موضوع")
    text = models.TextField(verbose_name="متن تیکت")
    is_readed = models.BooleanField(default=False,verbose_name="خوانده شده/نشده")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "تیکت ها"
        verbose_name_plural = "تیکت"