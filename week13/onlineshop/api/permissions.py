from rest_framework.permissions import BasePermission

from .constats import SELLER, CUSTOMER


class IsAllowedToCreateProduct(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == SELLER


class IsAllowedToCreateOrder(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == CUSTOMER
