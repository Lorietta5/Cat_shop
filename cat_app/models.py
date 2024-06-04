from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    available_quantity = models.IntegerField()
    photo = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
