from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=64, null=True)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
        
class Tag(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
            ('Indoor', 'Indoor'),
            ('Outdoor', 'Outdoor')
    )

    name = models.CharField(max_length=64, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=64, null=True, choices=CATEGORY)
    description = models.CharField(max_length=64, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, related_name='orders')
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name='orderBelongingTo')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=64, null=True, choices=STATUS)
    note = models.CharField(max_length=64, null=True)
    
    def __str__(self):
        return self.product.name