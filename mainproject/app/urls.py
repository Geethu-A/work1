from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('appoint/',views.appoint,name='appoint'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq,name='faq'),
    path('gallery/',views.gallery,name='gallery'),
    path('treatment/',views.treatment,name='treatment'),
    path('testimonials/',views.testimonials,name='testimonials')
]
