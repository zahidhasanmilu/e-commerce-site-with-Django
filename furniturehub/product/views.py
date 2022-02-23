from django.shortcuts import render
from .models import Product

# Create your views here.
def trending(request):
    products = Product.objects.all()
    data = {
        'product': products,
        'page_name':'Trending' 
    }           
    return render(request,'product/trending.html',data)  
    