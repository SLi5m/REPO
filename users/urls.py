from django.urls import path
from . import views

#create url patterns for the repo app here

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]