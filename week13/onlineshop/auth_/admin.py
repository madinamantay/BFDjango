from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import MyUser, Profile


class AdminProfile(admin.StackedInline):
    model = Profile
    verbose_name = 'Profile'
    verbose_name_plural = 'Profiles'
    can_delete = False


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    inlines = (AdminProfile,)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address', 'bio', )
