from django import forms
from .models import Item, ItemName

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'item',
            'brand_name',
            'uom',
            'quantity'
        )
        labels = {
            'item': 'Item Description',
            'brand_name': 'Brand Name',
            'uom': 'UOM',
            'quantity':'Quantity'
        }

        # widgets = {
        #     'item': forms.Select(attrs={'id':'item'}),
        #     'brand_name': forms.TextInput(attrs={'id':'brand'}),
        #     'uom': forms.TextInput(attrs={'id':'uom'}),
        #     'quantity': forms.TextInput(attrs={'id':'quantity'})
        # }
 