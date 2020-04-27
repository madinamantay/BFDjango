from django.db import models
from .validators import validate_extension, validate_file_size


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=100, blank=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}: {self.price}'

    class Meta:
        abstract = True


class ProductInfo(Product):
    # city = models.CharField(max_length=250, default="Almaty")
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)

    img = models.ImageField(upload_to='product_images',
                            validators=[validate_file_size,
                                        validate_extension],
                            null=True, blank=True)

    def _try_to_create_offer(self, created):
        if created:
            offer = f'In the shop appears exclusive product {self.name}'

            Offer.objects.get_or_create(title=offer)

    def _try_to_create_last_product_offer(self):
        offer = f'Do not miss the last one: {self.name}'

        Offer.objects.create(title=offer)

    def save(self, *args, **kwargs):
        created = self.id is None

        super(Product, self).save(*args, **kwargs)

        self._try_to_create_offer(created)

    def delete(self, *args, **kwargs):
        super(Product, self).delete()

        self._try_to_create_last_product_offer()


class OnlineProduct(Product):
    sale = models.CharField(max_length=250)
    status = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)

    def short_name(self):
        return self.name[:10]


class OfflineProduct(Product):
    address = models.CharField(max_length=250, default="Almaty")

    def short_name(self):
        return self.name[:5]


class Order(models.Model):
    discount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'order#{self.id}'


class ProductOrder(Order):
    product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    delivery_price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField()


class Offer(models.Model):
    title = models.TextField(max_length=300)

    def __str__(self):
        return self.title
