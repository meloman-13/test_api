from django.contrib import admin

from api.models import User, Image
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = BaseUserAdmin.list_display + ("plan",)
    fieldsets = BaseUserAdmin.fieldsets + (("Plan :", {"fields": ("plan",)}),)


admin.site.register(Image)
