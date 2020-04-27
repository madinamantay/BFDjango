from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


# Create your models here.
from .constant import SELLER, CUSTOMER, USER_ROLES


class MyUserManager(UserManager):
    def get_salesmen(self):
        return self.filter(role=SELLER)

    def get_customers(self):
        return self.filter(role=CUSTOMER)


class MyUser(AbstractUser):
    role = models.PositiveSmallIntegerField(choices=USER_ROLES, default=CUSTOMER)

    objects = MyUserManager()


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    address = models.TextField(default='Almaty')
    bio = models.CharField(max_length=250, default="Hello! I am there!")
