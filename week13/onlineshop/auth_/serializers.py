from rest_framework import serializers
from .models import MyUser


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'role')

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user
