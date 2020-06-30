from django.db import models
from django.conf import settings

# Create your models here.

class Item(models.Model):
	name = models.CharField(max_length=64)
	price = models.FloatField(blank=True)

	def __str__(self):
		return f"{self.name}: ${self.price}"

class CartItem(models.Model):
	item_reference = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.item_reference.name}: ${self.item_reference.price}"

class Cart(models.Model):
	ref_code = models.CharField(max_length=16, blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	items = models.ManyToManyField(CartItem, blank=True, related_name="items")
	order_status = models.CharField(max_length=100, blank=True)

