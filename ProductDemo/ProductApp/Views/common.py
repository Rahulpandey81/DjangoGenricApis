from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework import generics
from ProductApp.Views.serializer import UserSerializer, ProductSerializer, ShopSerializer
from ProductApp.models import *
import django_filters.rest_framework
import django_filters
from rest_framework import status
from rest_framework.response import Response
from django_filters.utils import translate_validation
import json
from django.views.decorators.csrf import csrf_exempt

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = products
        fields = ['price', 'productName','Id','brand__BrandName']

class productsList(generics.ListCreateAPIView):
    queryset = products.objects.all().order_by('-price')
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['Id', 'productName', 'brand__BrandName']

class shopList(generics.ListAPIView):
    queryset = shops.objects.all()
    serializer_class = ShopSerializer

class productDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = products.objects.all()
    serializer_class = ProductSerializer

  
@api_view(['GET', 'POST'])
@csrf_exempt
def product_list(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    filterset = ProductFilter(request.GET, queryset=products.objects.all())
    if not filterset.is_valid():
         raise translate_validation(filterset.errors)
    serializer = ProductSerializer(filterset.qs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        print(pk)
        product = products.objects.get(Id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

    

