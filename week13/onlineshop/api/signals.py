from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Product, Offer


@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    if created and instance.price < 3000:
        offer = f'In the shop appears exclusive product: {instance.name}'
        Offer.objects.create(title=offer)


@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, using, **kwargs):
    if len(Product.objects.all()) < 10:
        offer = f'Do not miss the last one: {instance.name}'
        Offer.objects.create(title=offer)
