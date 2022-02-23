from django.shortcuts import render
from .models import Product

# Create your views here.
def trending(request):
    products = Product.objects.all()
             
    return render(request,'product/trending.html', context={
        'product': products, 
        'page_name':'Trending'
        })  

