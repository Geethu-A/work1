from django.shortcuts import render

from . models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")
def contact(request):
    return render(request,"contact.html")    
def faq(request):
    return render(request,"faq.html")    
def gallery(request):
    return render(request,"gallery.html")   
def testimonials(request):
    return render(request,"testimonials.html")   
def treatment(request):
    return render(request,"treatment.html")                
def appoint(request):
    if request.method=='POST':
        d=Productform(request.POST)
        if d.is_valid():
            d.save()
            return index(request)
    return render(request,'appoint.html')