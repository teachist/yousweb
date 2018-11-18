from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory
from review.models import Review
from order.models import Order


class NewOrder(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['user', 'create_time', 'status']
