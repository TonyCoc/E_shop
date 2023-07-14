from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Profile_photo(models.Model):
    photo = models.ImageField(upload_to='users_profiles/',default='Def_prof/def.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE ,primary_key=True)

    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پزوفایل ها"

    def __str__(self):
        return self.user.get_username()


