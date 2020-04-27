from rest_framework import serializers
from .models import ProductInfo, Product, Offer

from .models import Order, ProductOrder


class ProductInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    color = serializers.CharField(max_length=50)
    size = serializers.CharField(max_length=10)

    def create(self, validated_data):
        product = ProductInfo.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price')


class ProductInfoShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInfo

        fields = ('id', 'name', 'price')


class ProductInfoFullSerializer(ProductInfoShortSerializer):
    class Meta(ProductInfoShortSerializer.Meta):
        fields = ProductInfoShortSerializer.Meta.fields + ('description', 'size', 'color')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'discount', 'price')


class ProductOrderSerializer(OrderSerializer):
    product = ProductInfoFullSerializer(read_only=True)

    product_id = serializers.IntegerField(write_only=True)

    class Meta(OrderSerializer.Meta):
        model = ProductOrder

        fields = OrderSerializer.Meta.fields + ('item', 'item_id', 'quantity')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer

        fields = ('title',)
