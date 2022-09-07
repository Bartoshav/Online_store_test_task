from rest_framework import viewsets,generics
from rest_framework.pagination import PageNumberPagination
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, StatsSerializer
from django.db.models.functions import Left, TruncMonth
from django.db.models import  Count, Sum 
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.http import JsonResponse

class APIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = APIListPagination

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = APIListPagination

class OrderFilter(filters.FilterSet):
    date_start = filters.DateFilter(field_name="Date", lookup_expr='gte',required=True)
    date_end = filters.DateFilter(field_name="Date", lookup_expr='lte',required=True)

    class Meta:
        model = Order
        fields = ['Date']

class StatsAPIView(generics.ListAPIView):
  
    serializer_class = StatsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter

    def get_queryset(self):
        metric = self.request.query_params.get('metric')
        if metric == 'count':
            queryset=Order.objects.values(month=TruncMonth('Date')).annotate(value = Count('id'))
        elif metric == 'price':
            queryset=Order.objects.values(month=TruncMonth('Date')).annotate(value = Sum('Product__price'))     
                       
        return queryset

def error_500(request):
    message = ("the metric parameter is required and should be 'count' or 'price'")
    response = JsonResponse(data={'message': message, 'status_code': 500})
    response.status_code =500
    return response