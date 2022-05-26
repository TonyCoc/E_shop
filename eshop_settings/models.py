from django.db import models


class Settings(models.Model):
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=250)
    phone = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    email = models.EmailField(max_length=80)
    Logo = models.ImageField(upload_to='Logo', null=True, blank=True)
    about = models.TextField(blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تنظیم سابت"
        verbose_name_plural = "تنظیمات سایت"
