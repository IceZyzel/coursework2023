from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'term', 'measure']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'phone', 'email', 'address', 'iban', 'rating', 'payment_method', 'delivery_method',
                  'products']


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = ['first_name', 'last_name', 'surname', 'phone']


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'amount', 'expired_at']


class CookerForm(forms.ModelForm):
    class Meta:
        model = Cooker
        fields = ['first_name', 'last_name', 'surname', 'phone', 'rank']


class SuppliesForm(forms.ModelForm):
    class Meta:
        model = Supplies
        fields = '__all__'


class CookerSelectionForm(forms.Form):
    cooker = forms.ModelChoiceField(queryset=Cooker.objects.all())


class CookerProductForm(forms.Form):
    stock = forms.ModelChoiceField(queryset=Stock.objects.all())
    amount = forms.IntegerField()
