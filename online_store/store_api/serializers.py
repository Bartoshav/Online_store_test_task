from rest_framework import serializers
from .models import Order, Product
from drf_writable_nested.serializers import WritableNestedModelSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OrderSerializer(WritableNestedModelSerializer):
    Product=ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'Date', 'Product']

class StatsSerializer(serializers.Serializer):
    month_report = serializers.DateField()
    value = serializers.IntegerField()