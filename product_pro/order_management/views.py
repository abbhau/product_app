from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm,formset
from .models import Order, OrderItem 
from django.http import JsonResponse
from .models import Product
from django.core.paginator import Paginator
from django.views import View
# Create your views here.

class AddProductView(View):
    def get(self, request):
        form = OrderForm()
        order = Order()
        orderitems_formset = formset(instance=order)
        context = {"form": form, "orderitems_formset": orderitems_formset}
        return render(request, "order_form.html", context)

    def post(self, request):
        # Bind the main order form
        form = OrderForm(request.POST)

        if form.is_valid():
            # Save the order instance
            order = form.save(commit=False)
            # Bind the orderitems formset with the order instance
            orderitems_formset = formset(request.POST, instance=order)

            if orderitems_formset.is_valid():
                # Save the main order instance
                order.save()

                # Save the associated order items
                orderitems = orderitems_formset.save(commit=False)
                for orderitem in orderitems:
                    orderitem.order = order
                    orderitem.save()
                order.calculate_total()

                # Redirect to a success page or another view
                return redirect("product_list")  # Replace 'order_success' with your success URL name

        else:
            # If the order form is invalid, initialize an empty formset for rendering
            orderitems_formset = formset(request.POST)
            print(form.errors)
            print(orderitems_formset.errors)
            print(orderitems_formset.non_form_errors())

        # If the form or formset is invalid, re-render the page with errors
        context = {"form": form, "orderitems_formset": orderitems_formset}
        return render(request, "order_form.html", context)
    

class UpdateProductView(View):
    def get(self, request, pk):
        # Retrieve the existing order by primary key (pk)
        order = get_object_or_404(Order, pk=pk)
        
        # Initialize the main order form and formset with the existing instance
        form = OrderForm(instance=order)
        orderitems_formset = formset(instance=order)
        
        context = {"form": form, "orderitems_formset": orderitems_formset, "order": order}
        return render(request, "order_form.html", context)

    def post(self, request, pk):
        # Retrieve the existing order by primary key (pk)
        order = get_object_or_404(Order, pk=pk)
        
        # Bind the main order form
        form = OrderForm(request.POST, instance=order)
        
        if form.is_valid():
            # Save the order instance
            order = form.save(commit=False)
            
            # Bind the orderitems formset with the order instance
            orderitems_formset = formset(request.POST, instance=order)
            
            if orderitems_formset.is_valid():
                # Save the main order instance
                order.save()

                # Save the associated order items
                orderitems = orderitems_formset.save(commit=False)
                for orderitem in orderitems:
                    orderitem.order = order
                    orderitem.save()

                # Delete removed items
                for orderitem in orderitems_formset.deleted_objects:
                    orderitem.delete()
                
                order.calculate_total()
                
                # Redirect to a success page or another view
                return redirect("product_list")  # Replace with your success URL name
        
        else:
            # If the order form is invalid, rebind the formset for rendering
            orderitems_formset = formset(request.POST, instance=order)
            print(form.errors)
            print(orderitems_formset.errors)
            print(orderitems_formset.non_form_errors())
        
        # If the form or formset is invalid, re-render the page with errors
        context = {"form": form, "orderitems_formset": orderitems_formset, "order": order}
        return render(request, "order_form.html", context)


def product_list_api(request):
    q = request.GET.get('q', '')  # Get the search term (user input)
    page = int(request.GET.get('page', 1))  # Get the page number, default to 1 if not provided

    # Define the number of items per page
    items_per_page = 10

    # Calculate the starting and ending index for pagination
    start = (page - 1) * items_per_page
    end = page * items_per_page

    # Filter the brands based on the search term (case-insensitive)
    products = Product.objects.filter(name__icontains=q)[start:end] 

    # Prepare the data in the expected format
    items = [{'id': product.id, 'product_name': product.name} for product in products]

    # Determine if more results are available
    total_count = Product.objects.filter(name__icontains=q).count()
    has_more = end < total_count

    # Return the results in the required format for Select2
    return JsonResponse({
        'items': items,
        'pagination': {'more': has_more} 
    })


