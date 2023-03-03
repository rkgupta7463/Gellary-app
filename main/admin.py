from django.contrib import admin
from .models import uploadImg
# Register your models here.

# class UsersAdmin(admin.ModelAdmin):
#     list_display=['email','first_name','last_name','date_joined','is_superuser','last_login','is_active','is_staff']

# admin.site.register(Users,UsersAdmin)

admin.site.register(uploadImg)