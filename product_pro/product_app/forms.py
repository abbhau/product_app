from django import forms
from .models import Product, Brand

class ProductForm(forms.ModelForm):
    brand = forms.ModelMultipleChoiceField(
        queryset= Brand.objects.none()
    )
    class Meta:
        model = Product
        fields = ['name', 'quantity', 'prize', 'brand']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'prize': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        brands = kwargs.pop('brands', None)  # Capture the brand data as a list
        super().__init__(*args, **kwargs)

        # Store the brands passed in the form initialization
        if brands:
            self.cleaned_brands = brands
        else:
            self.cleaned_brands = []

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
            # Update the ManyToManyField only after saving the product instance
            if hasattr(self, 'cleaned_brands'):
                product.brands.set(self.cleaned_brands)
        print(product.brands.all())
        return product