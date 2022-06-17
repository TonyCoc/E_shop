from rest_framework import serializers
from .models import Product

class Product_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id','title','description','price','active','free','views','teacher']