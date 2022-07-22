import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver



class Reset_password(models.Model):
    reset_code = models.CharField(max_length=6,null=True,unique=True,blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'کد بازگردانی رمز عبور'
        verbose_name_plural = 'کد های بازگردانی رمز عبور'

    reset_try_count = models.IntegerField(default=0)

    is_unvalidated = models.BooleanField(default=False)

    is_baned = models.BooleanField(default=False ,null=False ,blank=False)

@receiver(post_save,sender=User)
def post_save_Reset_code(instance , sender , created ,**kwargs ):
    if created:
            create_obj = Reset_password.objects.create(user = instance,reset_code = str(uuid.uuid4()).replace('-','').upper()[:6] )
            create_obj.save()

@receiver(pre_save,sender=Reset_password)
def pre_save_Reset_code(instance,sender,**kwargs):
    if instance.reset_try_count >= 5:
        instance.is_unvalidated = True
    else:
        instance.is_unvalidated = False
    if instance.reset_code is None:
        instance.reset_code = str(uuid.uuid4()).replace('-','').upper()[:6]

