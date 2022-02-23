from django.shortcuts import render
from product.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
   
    return render(request,'home/index.html', context={
        'product': products,
        'page_name':'Home Page'
        })


def search(request):
    return render(request, 'home/search_result.html')