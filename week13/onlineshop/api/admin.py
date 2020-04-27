from django.contrib import admin

from .models import ProductInfo, ProductOrder, Offer, OnlineProduct, OfflineProduct


@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'desc', 'color', 'size', 'img')


@admin.register(OnlineProduct)
class OnlineProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'desc', 'sale', 'status', )


@admin.register(OfflineProduct)
class OfflineProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'desc', 'address', )


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
