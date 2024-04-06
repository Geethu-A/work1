from django.shortcuts import render
from . models import *
from . form import *
# Create your views here.
def index(request):
    pld=Teacher.objects.all()
    return render(request,"index.html",{'pld':pld})
def form(request):
  
    if request.method=="POST":
        s=Teacher_form(request.POST)
        if s.is_valid():
            s.save()
            return index(request)
        else:
            print('invalid')
    return render(request,"form.html")