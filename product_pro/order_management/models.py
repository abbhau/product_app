from django.db import models
from product_app.models import Product
# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('processing', 'Processing'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending'
    )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"

    def calculate_total(self):
        """Calculate the total amount for the order based on the associated OrderItems."""
        self.total_amount = sum(item.total_price for item in self.order_items.all())
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True,related_name="ordered_products")
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        """Calculate the total price for this item."""
        return self.quantity * self.product_name.prize

    def __str__(self):
        return f"{self.quantity} x {self.product_name} (Order #{self.order.id})"

