from django.urls import path
from . import views

#create url patterns for the repo app here

urlpatterns = [
    path( '', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('contact_us/', views.contact_us, name='contact_us'),
]