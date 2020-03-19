from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def blogsingle(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')


def listings(request):
    return render(request, 'listings.html')


def listingssingle(request):
    return render(request, 'listings-single.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')