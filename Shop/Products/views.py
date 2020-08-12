from django.shortcuts import render
from .models import ProductsTable
from django.http import HttpResponse
# Create your views here.

#Select * from ProductsTable - list of products on a homepage
def index(request):
    query = ProductsTable.objects.all()
    return HttpResponse(query)