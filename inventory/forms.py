from django import forms
from .models import Item, ItemName

class ItemFormAdd(forms.ModelForm):
    class Meta:
        model = Item
        
        fields = [
            'item',
            'quantity',
            'remarks'
        ]

        labels = {
            'item': 'Item Description',
            'quantity':'Quantity',
            'remarks':'remarks',
        }

        widgets = {
            'item': forms.Select(attrs={'class':'item'}),
            'quantity': forms.TextInput(attrs={'class':'quantity'}),
            'remarks': forms.TextInput(attrs={'value': 'IN', 'type':'hidden'})           
        }
 
        item = forms.ModelChoiceField(
                queryset=ItemName.objects.all(),
                to_field_name='item',
                required=True,  
                widget=forms.Select(attrs={'class': 'form-control'})
            )
        
class ItemFormGet(forms.ModelForm):
    class Meta:
        model = Item
        
        fields = [
            'item',
            'quantity',
            'remarks'
        ]

        labels = {
            'item': 'Item Description',
            'quantity':'Quantity',
            'remarks':'remarks',
        }

        widgets = {
            'item': forms.Select(attrs={'class':'item'}),
            'quantity': forms.TextInput(attrs={'class':'quantity'}),
            'remarks': forms.TextInput(attrs={'value': 'OUT', 'type':'hidden'})           
        }
 
        item = forms.ModelChoiceField(
                queryset=ItemName.objects.all(),
                to_field_name='item',
                required=True,  
                widget=forms.Select(attrs={'class': 'form-control'})
            )
        
class ItemNameForm(forms.ModelForm):
    class Meta:
        model = ItemName
        fields = ['item_name','brand_name']
        widgets = {
            'item_name': forms.TextInput(attrs={'class':'item'}),
            'brand_name': forms.TextInput(attrs={'class':'brand_name'}),
        }

    
