from django.db import models

# Create your models here.
# Add more models here like ......... Smart Speakers, Wireless chargers, GPU's, CPU's , Motherboard


class Electronics(models.Model):

    type = models.CharField(max_length=256, blank=False)
    price = models.IntegerField()
    brand = models.CharField(max_length=256, null=True)
    choices = (
        ('AVAILABLE', 'Items to be PURCHASED'),
        ('SOLD', 'Item SOLD'),
        ('RESTOCKING', 'Items to be RESTOCKED')
    )
    status = models.CharField(max_length=100, choices=choices, default='SOLD')
    # sku = models.TextField(max_length=64, null=True)
    issues = models.CharField(max_length=100, default='No issues')
    shipping_choices = (
        ('SHIPPABLE', 'item can be shipped'),
        ('NON-SHIPPABLE', 'item cannot be shipped'),
        ('SPECIAL-SHIPPING', 'item will be shipped later')
        
    )
    shipping = models.CharField(
        max_length=100, choices=shipping_choices, default='SHIPPABLE')

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price : {1}'. format(self.type, self.price)


class laptops(Electronics):

    pass


class desktops(Electronics):
    pass


class smartphones(Electronics):
    pass


class headphones(Electronics):
    pass
