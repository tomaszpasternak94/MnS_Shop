from django.shortcuts import render
from .models import ProductsTable
from .models import CategoryTable
from django.http import HttpResponse
# Create your views here.

#Select * from CategoryTable - list of category type on a homepage
def index(request):
    #query_products_all = ProductsTable.objects.all()
    query_category_all = CategoryTable.objects.all()
    return HttpResponse(query_category_all)

def category(request, id):
    category_from_db = CategoryTable.objects.get(pk=id)
    return HttpResponse(category_from_db)
