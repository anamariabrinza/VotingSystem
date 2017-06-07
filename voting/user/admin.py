from django.contrib import admin
from .models import Group, User
# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('user_permissions', 'last_login')

