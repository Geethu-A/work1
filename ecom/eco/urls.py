from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name='index'),
    path('form/',views.form1,name='form'),
    path('form2/',views.form2,name='form2'),
    path('form3/',views.form3,name='form3'),
    path('update/<int:p>',views.edit_item,name='edit'),
    path('delete/<int:p>',views.delete_item,name='delete'),
]
