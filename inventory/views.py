from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def home(request):
    items = Item.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'items': items, 'form': ItemForm}
    return render(request,'inventory/home.html', context)


def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'inventory/add_item.html', context)


def delete_item(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)
        item.delete()
    return redirect('home')
    