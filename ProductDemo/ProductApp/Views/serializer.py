from rest_framework import serializers
from django.contrib.auth.models import User
from ProductApp.models import  *

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
class BrandSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Brands
        fields = ('Id', 'BrandName')       
        
class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.BrandName', read_only=True)
    brand = BrandSerilizer()
    class Meta:
        model = products
        fields = ("Id","productName", "price", "brand_name", "brand", "description")
    # def to_representation(self, data):
        # request = self.context.get("request")
        # if request and hasattr(request, "user"):
            # print(str(request.user))
        # data = super(ProductSerializer, self).to_representation(data)
        # data['productName'] = 'slow' 
        # return data
class ShopSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = shops
        fields = ("Id", "Name", "product")    
    