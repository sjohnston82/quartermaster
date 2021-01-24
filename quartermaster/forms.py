from django.forms import ModelForm
from django import forms
from .models import PantryItem, Category
import datetime

choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

class AddPantryItem(forms.ModelForm):
    class Meta:
        model = PantryItem
        fields = (
            'item_name',
            'quantity',
            'expiration_date',
            
            'category',
        )
        item_name = forms.CharField(max_length=255)
        # expiration_date = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        quantity = forms.IntegerField()
        
        
        widgets = {
            'expiration_date' : forms.DateInput(attrs={'type': 'date'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }