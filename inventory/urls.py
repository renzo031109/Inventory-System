from django.urls import path, include
from . import views

urlpatterns = [
    path('delete_itembase/<str:item_code>/', views.delete_itembase, name = 'delete_itembase'),
    path('delete/<str:id>/', views.delete_item, name = 'delete_item'),
    path('summary/', views.summary_item, name='summary_item'),
    path('inventory/', views.inventory_item, name='inventory_item'),
    path('', views.get_item, name='get_item'),
    path('new_item/', views.new_item, name='new_item'),
    path('add_item/', views.add_item, name='add_item'),
    path('submitted/', views.submitted, name='submitted'),
    path('export_file_inventory/', views.export_excel_inventory, name='export_file_inventory'),
    path('export_file_summary/', views.export_excel_summary, name='export_file_summary'),

]
