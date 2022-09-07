from django.db import models

class Product(models.Model):
    title = models.CharField (max_length=200, blank=False)
    price = models.DecimalField (max_digits=12, decimal_places=2, blank=False)

    def __str__(self):
        return self.title

class Order(models.Model):
    Date= models.DateField(auto_now_add=True)
    Product = models.ManyToManyField(Product)
