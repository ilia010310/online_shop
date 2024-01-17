from django import forms
from django_summernote.widgets import SummernoteWidget
from order.models import Order


class OrderForm(forms.ModelForm):
    customer_name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={"class": "form-control",
                                                         'placeholder': 'Контактное лицо', 'style': 'width: 300px;'}))
    customer_email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={"class": "form-control",
                                                            'placeholder': 'Email', 'style': 'width: 300px;'}))
    customer_phone = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Телефон',
                                                         'style': 'width: 300px;'}))
    customer_inn = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'ИНН (для юр. лиц)',
                                                         'style': 'width: 300px;'}))
    comments = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Комментарий к заказу',
                                                         'style': 'width: 300px; height: 100px;'}))
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone',
                  'customer_inn',  'comments']