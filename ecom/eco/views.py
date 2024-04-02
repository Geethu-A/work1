from django.shortcuts import render
from . models import *
from .forms import *
# Create your views here.
def index(request):
    pld=Product.objects.all()
    return render(request,"index.html",{'pld':pld})

#built-in form
def form1(request):
    d=Productform()
    if request.method=='POST':
        d=Productform(request.POST)
        if d.is_valid():
            d.save()
            return index(request)
    return render(request,'form1.html',{'form':d})

# user defined without using objects
def form2(request):
    if request.method=='POST':
        d=Productform(request.POST)
        if d.is_valid():
            d.save()
            return index(request)
    return render(request,'form2.html')

# user-defined with using objects
def form3(request):
    if request.method=='POST':
        name1=request.POST.get('n')
        s=Product.objects.create(name=name1)
        s.save()
        return index(request)
    return render(request,'form3.html')
#update
def edit_item(request,p):
    b=Product.objects.get(pk=p)
    f=Productform(instance=b)
    if request.method=='POST':
        f=Productform(request.POST,instance=b)
        if f.is_valid():
            f.save()
            return index(request)
    return render(request,'edit.html',{'form':f})
def delete_item(request,p):
    b=Product.objects.get(pk=p)
    b.delete()
    return index(request)
        

