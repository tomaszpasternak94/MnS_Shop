from django.contrib import admin
from .models import ProductsTable
from .models import CategoryTable

# Register your models here.

admin.site.register(ProductsTable)
admin.site.register(CategoryTable)
