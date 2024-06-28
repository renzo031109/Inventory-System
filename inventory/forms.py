from django import forms
from django.forms import modelformset_factory
from .models import Item, ItemBase

        
class ItemNewForm(forms.ModelForm):
    class Meta:
        model = ItemBase
        fields = ['item_name','brand_name','soh','uom','price','item_code','remarks']
        labels = {
            'item_name': 'ITEM NAME',
            'brand_name': 'BRAND NAME (NONE if N/A)',
            'soh': 'BEGINNING BALANCE',
            'price': 'PRICE',
            'item_code': 'ITEM CODE',
            'uom':'UOM',
            'remarks' : 'REMARKS'

        }
        widgets = {
            'item_name': forms.TextInput(attrs={'class':'ItemNewForm','autocomplete': 'off'}),
            'brand_name': forms.TextInput(attrs={'class':'ItemNewForm', 'value':'NONE', 'autocomplete': 'off'}),
            'soh': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'uom': forms.Select(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'price': forms.TextInput(attrs={'class':'ItemNewForm', 'autocomplete': 'off'}),
            'item_code': forms.TextInput(attrs={'class':'ItemNewForm','autocomplete': 'off','type':'hidden'}),
            'remarks': forms.TextInput(attrs={'value': 'OUT', 'type':'hidden'}) 
        }

ItemModelFormSet = modelformset_factory(
    Item, 
    fields=('item_code','quantity','item_name','brand_name','staff_name','client_name','department_name'),
    extra=1,
    labels={
        'staff_name': 'STAFF NAME',
        'client_name': 'CLIENT NAME',
        'dapartment_name': 'DEPARTMENT NAME'
    },
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
            }),
        'item_name': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            }),
        'brand_name': forms.TextInput(attrs={
            'class':'form-control',
            'type':'hidden'
            }),
        'staff_name': forms.TextInput(attrs={
            'class':'form-control',
     
            }),
        'client_name': forms.Select(attrs={
            'class':'form-control',
 
            }),
        'department_name': forms.Select(attrs={
            'class':'form-control',
       
            }),

    }
)


