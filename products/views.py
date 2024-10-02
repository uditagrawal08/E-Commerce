from django.shortcuts import render
from products.models import Product

# Create your views here.

def get_products(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        return render(request,'product/product.html',context={'product':product})
    
    except Exception as e:
        return render(request,'home/index.html')