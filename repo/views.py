from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'repo/home.html')


def blog(request):
    return render(request, 'repo/blog.html')


def about(request):
    return render(request, 'repo/about.html')


def services(request):
    return render(request, 'repo/services.html')


def contact_us(request):
    return render(request, 'repo/contact_us.html')
