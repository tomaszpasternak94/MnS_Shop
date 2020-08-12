from django.db import models

# Create your models here.

class CategoryTable(models.Model):
    type = models.CharField(max_length=50)

    # This function returns the category type in the admin panel
    def __str__(self):
        return self.type


class ProductsTable(models.Model):
    #Foreign key (CategoryTable)
    category = models.ForeignKey(CategoryTable, on_delete=models.CASCADE, null=True)

    #Fields of ProductsTable
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    #This function returns names of products in the admin panel
    def __str__(self):
        return self.name