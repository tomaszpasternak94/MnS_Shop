from django.db import models

# Create your models here.

class ProductsTable(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    # This function returns names of products in the admin panel
    def __str__(self):
        return self.name
