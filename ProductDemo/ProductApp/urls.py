"""ProductDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from ProductApp.Views import common
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('api/products', common.productsList.as_view()),
    path('api/shops', common.shopList.as_view()),
    path('api/products/<int:pk>', common.productDetails.as_view()),
    path('products/new', common.product_list),
    path('product/new/<int:pk>',common.product_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)