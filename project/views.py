from django.shortcuts import render
from store.models import Product

def abc(request):
    data=Product.objects.all()
    context={'data':data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")
