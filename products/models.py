from django.db import models
from simple_history.models import HistoricalRecords
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProductModel(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    is_available = models.BooleanField(default=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.name}'


@receiver(post_save, sender=ProductModel)
def update_is_available(sender, instance, **kwargs):
    if instance.stock == 0 and instance.is_available:
        instance.is_available = False
        instance.save(update_fields=['is_available'])
    elif instance.stock > 0 and not instance.is_available:
        instance.is_available = True
        instance.save(update_fields=['is_available'])