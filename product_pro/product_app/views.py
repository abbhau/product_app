from django.shortcuts import render,get_object_or_404
from .serializers import Product, ProductSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.db.models import Q
from .pagination import CustomPagination
from django.http import HttpResponse
import csv

         
class ProductCreate(generics.CreateAPIView):
    ''' Create a Product in Product Model'''
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    ''' Retrive all Products of Product Model also custom pagination class is use 
        to retrieve 100 objects per page for goes on any page simply pass the page_no 
        value to 'page'query parameter .
    '''
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    ''' Retrieve single record from databse '''

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


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


def product_list(request):
    '''Fetch data and show on product list page using datatble serverside '''
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
        order_column_index = int(request.GET.get('order[0][column]', 0)) -1 #exclude sr no
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

        # Column-specific filters with validation
        if search_columns[0]:  # ID column
            if not search_columns[0].isdigit():
                return JsonResponse({"error": "ID must be an integer."}, status=400)
            queryset = queryset.filter(id=int(search_columns[0]))
        if search_columns[1]:  # Name column
            queryset = queryset.filter(name__icontains=search_columns[1])
        if search_columns[2]:  # Quantity column
            if not search_columns[2].isdigit():
                return JsonResponse({"error": "Quantity must be an integer."}, status=400)
            queryset = queryset.filter(quantity=int(search_columns[2]))
        if search_columns[3]:  # Prize column
            try:
                prize = float(search_columns[3])
                queryset = queryset.filter(prize=prize)
            except ValueError:
                return JsonResponse({"error": "Prize must be a number."}, status=400)
        if search_columns[4]:  # Total Prize column
            try:
                total_prize = float(search_columns[4])
                queryset = queryset.filter(total_prize=total_prize)
            except ValueError:
                return JsonResponse({"error": "Total prize must be a number."}, status=400)

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


def delete_product(request,pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


def product_list_csv(request):
    # Extract column-specific search terms
    search_columns = []
    for i in range(5):  # Number of columns in the table
        search_value = request.GET.get(f'columns[{i}][search][value]', '').strip()
        search_columns.append(search_value)

        # Get the column to sort by and the sort direction
    order_column_index = int(request.GET.get('order[0][column]', 0)) -1 #exclude sr no
    order_dir = request.GET.get('order[0][dir]', 'asc')  # Default direction is ascending
    
    # Get the column name to sort by
    columns = ['id', 'name', 'quantity', 'prize', 'total_prize']
    order_column = columns[order_column_index]  # Get the name of the column to sort by

    # Query the database
    queryset = Product.objects.all()
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

    
    # Create the CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'
    writer = csv.writer(response)
    
    # Write the CSV headers
    writer.writerow(['ID', 'Name', 'Quantity', 'Prize', 'Total Prize'])
    
    # Write the data rows
    for product in queryset:
        writer.writerow([product.id, product.name, product.quantity, product.prize, product.total_prize])

    return response


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# Product Create View
def product_create_view(request):
    if request.method == "POST":
        brands = request.POST.getlist('brand')
        form = ProductForm(request.POST, brands=brands)
        if form.is_valid():
            form.save()
            messages.success(request, "Product created successfully!")
            return redirect('product_list')  # Change 'product_list' to your target URL
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

# Product Update View
def product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('product_list')  # Change 'product_list' to your target URL
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})



from django.http import JsonResponse
from .models import Brand
from django.core.paginator import Paginator

def brand_list_api(request):
    q = request.GET.get('q', '')  # Get the search term (user input)
    page = int(request.GET.get('page', 1))  # Get the page number, default to 1 if not provided

    # Define the number of items per page
    items_per_page = 10

    # Calculate the starting and ending index for pagination
    start = (page - 1) * items_per_page
    end = page * items_per_page

    # Filter the brands based on the search term (case-insensitive)
    brands = Brand.objects.filter(brand_name__icontains=q)[start:end] 

    # Prepare the data in the expected format
    items = [{'id': brand.id, 'brand_name': brand.brand_name} for brand in brands]

    # Determine if more results are available
    total_count = Brand.objects.filter(brand_name__icontains=q).count()
    has_more = end < total_count

    # Return the results in the required format for Select2
    return JsonResponse({
        'items': items,
        'pagination': {'more': has_more} 
    })
