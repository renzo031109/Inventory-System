import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import Item, ItemBase
from django import forms


remarks_select = (
    ('IN', 'IN'),
    ('OUT', 'OUT'),
    ('BEGINNING','BEGINNING')
)




class DateInput(forms.DateInput):
    input_type = 'date'


class ItemFilter(django_filters.FilterSet):
    item_name = CharFilter(field_name='item_name', lookup_expr='icontains', label="ITEM NAME")
    brand_name = CharFilter(field_name='brand_name', lookup_expr='icontains', label="BRAND NAME")
    remarks = ChoiceFilter(field_name='remarks', label="REMARKS", choices=remarks_select)
    date_added = DateFilter(field_name='date_added', lookup_expr='gte', label="DATE ADDED FROM", widget=DateInput(attrs={'type': 'date'}))


    class Meta:
        model = Item
        fields = ['item_name','brand_name','remarks','date_added']


