from django.contrib import admin
from .models import *



class ticket_admin(admin.ModelAdmin):
    list_display = ['full_name','is_readed','subject']
    list_filter = ['is_readed']
    list_editable = ['is_readed']
admin.site.register(Contact_us_model,ticket_admin)