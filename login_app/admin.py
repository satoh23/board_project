from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Posts, Thread
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('nickname',)}),)
    list_display = ['username', 'email', 'nickname']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Posts)
admin.site.register(Thread)