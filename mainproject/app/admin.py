from django.contrib import admin
from . models import *
# Register your models here.
class Product_display(admin.ModelAdmin):
    list_display=['name','email','phone','date','time','message']
admin.site.register(Appointmentsss,Product_display)
