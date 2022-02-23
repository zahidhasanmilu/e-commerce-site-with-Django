from django.shortcuts import render
from product.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    data = {
        'product': products,
        'page_name':'Home Page' 
    }
    return render(request,'home/index.html', data)

    