from django.db import models

class membership(models.Model):
    email = models.EmailField()

    class Meta:
        verbose_name = "عضویت"
        verbose_name_plural = "عضویت ها"

    def __str__(self):
        return self.email