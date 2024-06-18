from django import forms
from django.forms import modelformset_factory
from .models import Item, ItemBase


uom_select = [
    ("1", "PIECE"), 
    ("2", "BOX"), 
    ("3", "PAD"), 
    ("4", "PACK"), 
    ("5", "REAM"), 
    ("6", "ROLL"),
]

        
class ItemNewForm(forms.ModelForm):
    class Meta:
        model = ItemBase
        fields = ['item_name','brand_name','soh','uom','price','item_code','remarks']
        labels = {
            'item_name': 'ITEM NAME',
            'brand_name': 'BRAND NAME',
            'soh': 'BEGINNING BALANCE',
            'price': 'PRICE',
            'item_code': 'ITEM CODE',
            'uom':'UOM',
            'remarks' : 'REMARKS'

        }
        widgets = {
            'item_name': forms.TextInput(attrs={'class':'ItemNewForm','autocomplete': 'off'}),
            'brand_name': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'soh': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'uom': forms.Select(choices = uom_select, attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'price': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'item_code': forms.TextInput(attrs={'class':'ItemNewForm','autocomplete': 'off','type':'hidden'}),
            'remarks': forms.TextInput(attrs={'value': 'OUT', 'type':'hidden'}) 
        }

ItemModelFormSet = modelformset_factory(
    Item, 
    fields=('item_code','quantity'),
    extra=1,
    widgets={
        'item_code': forms.Select(attrs={
            'class':'form-control form-select',
            'autocomplete': 'off'
            }),
        'quantity': forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': '0',
            'autocomplete': 'off'
            }),
        'remarks': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            })
    }
)


