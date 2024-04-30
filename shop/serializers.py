from rest_framework import serializers

from shop.models import ProductsModel


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = ('id', 'name', 'description', 'price', 'discount_price', 'cover_image', 'rating')