from django import forms
from django.forms import modelformset_factory
from .models import Item, ItemBase


# class ItemFormAdd(forms.ModelForm):
#     class Meta:
#         model = Item
        
#         fields = [
#             'item',
#             'quantity',
#             'remarks'
#         ]

#         labels = {
#             'item': 'Item Description',
#             'quantity':'Quantity',
#             'remarks':'remarks',
#         }

#         widgets = {
#             'item': forms.Select(attrs={'id':'select-item'}),
#             'quantity': forms.TextInput(attrs={'class':'quantity'}),
#             'remarks': forms.TextInput(attrs={'value': 'IN', 'type':'hidden'})           
#         }
 
        
class ItemFormGet(forms.ModelForm):
    class Meta:
        model = Item
        
        fields = [
            'item_name',
            'quantity',
            'remarks'
        ]

        labels = {
            'item_name': 'Item Description',
            'quantity':'Quantity',
            'remarks':'remarks',
        }

        widgets = {
            'item_name': forms.Select(attrs={'class':'select-item'}),
            'quantity': forms.TextInput(attrs={'class':'quantity'}),
            'remarks': forms.TextInput(attrs={'value': 'OUT', 'type':'hidden'})           
        }
 

        
class ItemNewForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','brand_name','price','soh']
        labels = {
            'item_name': 'Item Name',
            'brand_name': 'Brand Name',
            'price': 'Price',
            'soh': 'Beginning Balance',

        }
        widgets = {
            'item_name': forms.TextInput(attrs={'class':'item','autocomplete': 'off'}),
            'brand_name': forms.TextInput(attrs={'class':'brand_name', 'autocomplete': 'off'}),
            'price': forms.TextInput(attrs={'class':'price', 'autocomplete': 'off'}),
            'soh': forms.TextInput(attrs={'class':'soh', 'autocomplete': 'off'}),
        }


ItemModelFormSet = modelformset_factory(
    Item, 
    fields=('code','quantity'),
    extra=1,
    widgets={
        'code': forms.Select(attrs={
            'class':'form-control',
            'placeholder': 'Item'
            }),
        'quantity': forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': '0'
            })
    }
)


# from django.forms import ModelForm

# class ItemFormAdd(ModelForm):
#     class Meta:
#       model = Item
#       fields = ["item", "quantity", "remarks"]

# ItemFormSet = modelformset_factory(
#     Item, fields=("item", "quantity", "remarks"), extra=1
# )

# ItemModelFormset = modelformset_factory(
#     Item,
#     fields=('item','quantity','remarks' ),
#     extra=1,
#     widgets={
#         'item': forms.Select(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter Item Name here'
#             }
#         ), 
#         'quantity': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter quantity here'
#                 }
#         ),
#         'remarks': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'enter remarks'
#                 }
#         )
#     }
# )
