from django import forms
from .models import Item, ItemName

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'item',
            'quantity'
        )
        labels = {
            'item': 'Item Description',
            'quantity':'Quantity',
            
        }

        # widgets = {
        #     'item': forms.Select(attrs={'id':'item'}),
        #     'quantity': forms.TextInput(attrs={'id':'quantity'})
            
        # }
 
        item = forms.ModelChoiceField(
                queryset=ItemName.objects.all(),
                to_field_name='item',
                required=True,  
                widget=forms.Select(attrs={'class': 'form-control'})
            )