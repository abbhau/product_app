from django.shortcuts import render
from .serializers import Product, ProductSerializer, ProductRetriveSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#from rest_framework_simplejwt.authentication import JWTAuthentication
from .pagination import CustomPagination
         
class ProductCreate(generics.CreateAPIView):
    ''' Create a Product in Product Model'''
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    ''' Retrive all Products of Product Model also custom pagination class is use 
        to retrieve 4 objects per page for goes on any page simply pass the page_no 
        value to 'page'query parameter .
    '''
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    queryset = Product.objects.all()
    serializer_class = ProductRetriveSerializer


class ProductDetail(generics.RetrieveAPIView):
    ''' Retrieve single record from databse '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductRetriveSerializer


class ProductUpdate(generics.UpdateAPIView):
    '''Update the record from databse by using id '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDelete(generics.DestroyAPIView):
    '''To delete the single record by using id '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.db.models import Q
def product_list(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Server-side processing for DataTables
        draw = int(request.GET.get('draw', 1))
        start = int(request.GET.get('start', 0))
        length = int(request.GET.get('length', 10))

        # Extract column-specific search terms
        search_columns = []
        for i in range(5):  # Number of columns in the table
            search_value = request.GET.get(f'columns[{i}][search][value]', '').strip()
            search_columns.append(search_value)

         # Get the column to sort by and the sort direction
        order_column_index = int(request.GET.get('order[0][column]', 0))  # Default column is the first one
        order_dir = request.GET.get('order[0][dir]', 'asc')  # Default direction is ascending
        
        # Get the column name to sort by
        columns = ['id', 'name', 'quantity', 'prize', 'total_prize']
        order_column = columns[order_column_index]  # Get the name of the column to sort by

        # Query the database
        queryset = Product.objects.all()
        total_records = queryset.count()
         # Global search (applied to all columns)

        prize_range = request.GET.get('price_range', '')
        if prize_range:
            prize_range_start = prize_range.split("-")[0]
            prize_range_end = prize_range.split("-")[1]
            queryset = queryset.filter(
                total_prize__range=(prize_range_start, prize_range_end)
            )
        global_search_value = request.GET.get('search[value]', '').strip()
        if global_search_value:
            queryset = queryset.filter(
                Q(name__icontains=global_search_value) |
                Q(quantity__icontains=global_search_value) |
                Q(prize__icontains=global_search_value) |
                Q(total_prize__icontains=global_search_value)
            )

        # Column-specific filters
        if search_columns[0]:  # ID column
            queryset = queryset.filter(id=search_columns[0])
        if search_columns[1]:  # Name column
            queryset = queryset.filter(name__icontains=search_columns[1])
        if search_columns[2]:  # Quantity column
            queryset = queryset.filter(quantity=search_columns[2])
        if search_columns[3]:  # Prize column
            queryset = queryset.filter(prize=search_columns[3])
        if search_columns[4]:  # Total Prize column
            print(search_columns[4])
            queryset = queryset.filter(total_prize=search_columns[4])
        
        if order_dir == 'asc':
            queryset = queryset.order_by(order_column)  # Ascending order
        else:
            queryset = queryset.order_by(f'-{order_column}')  # Descending order

        # Pagination
        filtered_records = queryset.count()
        products = queryset[start:start + length]
        # Build the response data
        data = [
            {
                "id": product.id,
                "name": product.name,
                "quantity": product.quantity,
                "prize": product.prize,
                "total_prize": product.total_prize,
            }
            for product in products
        ]

        return JsonResponse({
            "draw": draw,
            "recordsTotal": total_records,
            "recordsFiltered": filtered_records,
            "data": data,
        })

    # Render the template for non-AJAX requests
    return render(request, "product_list.html")
