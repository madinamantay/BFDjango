from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.

class MyUserManager(UserManager):
    def create_editor(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_editor', True)
        return self._create_user(username, email, password, **extra_fields)


class MyUser(AbstractUser):
    pass
#     is_editor = models.BooleanField(default=False)
#     objects = MyUserManager()
#
#     # class Meta:
#     #     permissions = ('can_edit', 'Can edit')
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500)
#
#     def __str__(self):
#         return self.user.username