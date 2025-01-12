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
            self.fields['brand'].queryset = Brand.objects.filter(id__in=brands)

        elif self.instance and self.instance.pk:
            self.fields['brand'].initial = self.instance.brand.all()

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
            product.total_prize = product.quantity * product.prize
            # Update the ManyToManyField only after saving the product instance
            product.brand.set(self.cleaned_data['brand'])
            product.save()
        return product