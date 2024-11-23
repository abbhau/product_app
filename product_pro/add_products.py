import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_pro.settings')
django.setup()

from product_app.models import Product

products = []
for i in range(1, 100000000001):
    name = f'Product-{i}'
    quantity = random.randint(1, 100)
    prize = round(random.uniform(10.0, 100.0), 2)
    total_prize = quantity * prize
    products.append(
        Product(
            name=name,
            quantity=quantity,
            prize=prize,
            total_prize=total_prize,
        )
    )
Product.objects.bulk_create(products, batch_size=1000)
print('100,000 products added successfully!')
