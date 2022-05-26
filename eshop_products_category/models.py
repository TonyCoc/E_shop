from django.db import models


class category(models.Model):
    title = models.CharField(max_length=150,verbose_name="عنوان در سایت")
    name = models.CharField(max_length=150,verbose_name="عنوان در یو آر ال")
    active = models.BooleanField(default=False,verbose_name="وضعیت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی ها'
        verbose_name_plural = "دسته بندی"