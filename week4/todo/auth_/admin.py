from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import MyUser


# class InlineProfile(admin.StackedInline):
#     model = Profile
#     verbose_name = 'Profile'
#     verbose_name_plural = 'Profiles'
#     can_delete = False


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id', 'bioUser', 'user')
