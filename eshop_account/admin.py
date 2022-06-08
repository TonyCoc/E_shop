from django.contrib import admin
from .models import Reset_password


class admin_model(admin.ModelAdmin):
    list_display = ["user",'reset_code','is_unvalidated']
admin.site.register(Reset_password,admin_model)
