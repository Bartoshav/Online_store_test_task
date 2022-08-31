from rest_framework import viewsets,generics
from rest_framework.pagination import PageNumberPagination
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, StatsSerializer
from django.db.models.functions import Left
from django.db.models import  Count 

class APIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = APIListPagination

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = APIListPagination

class StatsAPIView(generics.ListAPIView):
    queryset=Order.objects.values(month_report=Left('Date',7)).annotate(value = Count('id'))
    serializer_class = StatsSerializer