from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # path('add_item/', views.add_item, name='add_item'),
    path('delete/<str:id>/', views.delete_item, name = 'delete_item'),
    path('summary/', views.summary_item, name='summary_item'),
    path('get_item/', views.get_item, name='get_item'),
    path('new_item/', views.new_item, name='new_item'),
    path('add_item/', views.BirdAddView.as_view(), name='add_item'),

]
