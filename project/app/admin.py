from django.contrib import admin
from . models import *
# Register your models here.
class College_display(admin.ModelAdmin):
    list_display=['dept']
admin.site.register(College,College_display) 
class Teacher_display(admin.ModelAdmin):
    list_display=['name','age','dept']
admin.site.register(Teacher,Teacher_display)