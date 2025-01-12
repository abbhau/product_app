from django.forms import inlineformset_factory
from .models import Order, OrderItem
from django import forms
from product_app.models import Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class OrderItemForm(forms.ModelForm):
    product = forms.IntegerField()
    class Meta:
        model = OrderItem
        fields = ['quantity']

        widgets = {
            "quantity" :forms.NumberInput(attrs={
                'class': 'form-control',
            })
        }

    def clean_product(self):
        product_id = self.cleaned_data["product"]
        product = Product.objects.filter(id=product_id).first()
        return product

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['product'].initial = self.instance.product_name
        else:
            self.fields['product'].queryset = Product.objects.none()

    def save(self, commit=True):
        orderitem = super().save(commit=False)
        orderitem.product_name = self.cleaned_data['product']
        orderitem.save()
        return orderitem


formset = inlineformset_factory(
    Order,
    OrderItem,
    form=OrderItemForm,
    extra=0,
    min_num=1,
    can_delete=True,
    max_num=1000,
)