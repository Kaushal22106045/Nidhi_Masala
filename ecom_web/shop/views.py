from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
import math

# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//3 + math.ceil(n/3 - n//3)
    allProds = []
    catProds = Product.objects.values('category', 'id')
    catgs = {item['category'] for item in catProds}
    for cat in catgs:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//3 + math.ceil(n/3 - n//3)
        allProds.append((prod, range(1,nSlides), nSlides))
    # params = {'no_of_slides' : nSlides, 'range' : range(1,nSlides), 'product':products} 
    # allProds = [(products, range(1,nSlides), nSlides),
    #           (products, range(1,nSlides), nSlides)]
    params = {'allProds' : allProds} 
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")    

def tracker(request):   
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def prodView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")

