from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm

@login_required
def home(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request,'inventory/home.html', context)

@login_required
def add_item(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'inventory/add_item.html', context)

@login_required
def delete_item(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)
        item.delete()
    return redirect('home')

def summary_item(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'inventory/summary.html', context)
    