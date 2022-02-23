from django.shortcuts import render

# Create your views here.
def home(request):
    page_name = 'Home Page'
    return render(request,'home/index.html', context= {'page_name':page_name})