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

def service_type(request, id):
    service_type_from_db = ProductsTable.objects.get(pk=id)
    show_type_descritpion_price = "<h1>" + str(service_type_from_db.name) +"</h1>" + \
                                  "<p>" + str(service_type_from_db.description) + "</p>" + \
                                  "<p>" + str(service_type_from_db.price) + "</p>"

    return HttpResponse(show_type_descritpion_price)