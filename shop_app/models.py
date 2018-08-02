from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    category = models.ForeignKey('Category', related_name="products",on_delete='CASCADE', null=True) 
    def __str__(self):
        return self.title
    def get_absolute_url(self): 
        return reverse('product_detail', args=[str(self.id)])

class Category(models.Model): 
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    #products = models.ForeignKey('Product', related_name="products",on_delete='CASCADE', null=True)
    def __str__(self):
        return self.title

class Order(models.Model): 
    product = models.ForeignKey(Product, on_delete='CASCADE') 
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)