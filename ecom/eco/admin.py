from django.contrib import admin
from . models import *
# Register your models here.
class Product_display(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Product,Product_display)
