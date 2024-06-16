from django import forms
from django.forms import modelformset_factory
from .models import Item, ItemBase


        
# class ItemFormGet(forms.ModelForm):
#     class Meta:
#         model = Item
        
#         fields = [
#             'item_code',
#             'quantity',
#             'remarks'
#         ]

#         labels = {
#             'item_code': 'Item Description',
#             'quantity':'Quantity',
#             'remarks':'remarks',
#         }

#         widgets = {
#             'item_code': forms.Select(attrs={'class':'select-item'}),
#             'quantity': forms.TextInput(attrs={'class':'quantity'}),
#             'remarks': forms.TextInput(attrs={'value': 'OUT', 'type':'hidden'})           
#         }
 

        
class ItemNewForm(forms.ModelForm):
    class Meta:
        model = ItemBase
        fields = ['item_name','brand_name','soh','price','item_code','remarks']
        labels = {
            'item_name': 'Item Name',
            'brand_name': 'Brand Name',
            'soh': 'Beginning Balance',
            'price': 'Price',
            'item_code': 'Item Code',
            'remarks' : 'Remarks'

        }
        widgets = {
            'item_name': forms.TextInput(attrs={'class':'ite_name','autocomplete': 'off'}),
            'brand_name': forms.TextInput(attrs={'class':'brand_name', 'autocomplete': 'off'}),
            'soh': forms.TextInput(attrs={'class':'soh', 'autocomplete': 'off'}),
            'price': forms.TextInput(attrs={'class':'price', 'autocomplete': 'off'}),
            'item_code': forms.TextInput(attrs={'class':'item_code','autocomplete': 'off','type':'hidden'}),
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


