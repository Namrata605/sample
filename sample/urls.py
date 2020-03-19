"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import view
from homepage import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('homepage.urls')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-single/', views.blogsingle, name='blog-single'),
    path('contact/', views.contact, name='contact'),
    path('listings/', views.listings, name='listings'),
    path('listings-single/', views.listingssingle, name='listings-single'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    # path('something/', view.something),
]
