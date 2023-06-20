from django import forms

from orders_app.models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': "Abdulla"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': "Abdullayev"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder': "example@mail.com"
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': "Farg'ona, Farg'ona, Ozodlik ko'chasi, 22-uy"
    }))

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", "address")