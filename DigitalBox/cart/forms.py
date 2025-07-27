from django import forms

class OrderCreateForm(forms.Form):
    customer_name  = forms.CharField(label='Ваше имя', max_length=100)
    customer_email = forms.EmailField(label='E‑mail')