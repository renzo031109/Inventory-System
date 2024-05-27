from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Item_SOH
from .forms import ItemFormGet, ItemFormAdd

@login_required
def home(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request,'inventory/home.html', context)

@login_required
def add_item(request):
    
    if request.method == 'POST':
        form = ItemFormAdd(request.POST)
        if form.is_valid():
            #get the item name from the form
            add_item = request.POST.get('item')
            #get the item qty from the form
            add_qty = request.POST.get('quantity')
            #get the item SOH from model table
            item_soh = Item_SOH.objects.get(item=add_item)
            #compute add soh
            soh = int(item_soh.soh) + int(add_qty)
            #get the updated soh after add
            item_soh.soh = soh
            #save tables
            item_soh.save()
            form.save()
            return redirect('home')
    else:
        form = ItemFormAdd()
    context = {'form': form}
    return render(request, 'inventory/add_item.html', context)

@login_required
def delete_item(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)
        item_soh = Item_SOH.objects.get(item=item.item)

        updated_soh = int(item_soh.soh) + int(item.quantity)
        item_soh.soh = updated_soh
        item_soh.save()
        item.delete()
    return redirect('home')

def summary_item(request):
    items = Item_SOH.objects.all()
    context = {'items': items}
    return render(request, 'inventory/summary.html', context)


def get_item(request):
    

    if request.method == 'POST':
        form = ItemFormGet(request.POST)    
        if form.is_valid():
            #get the item name from the form
            pick_item = request.POST.get('item')
            #get the item qty from the form
            pick_qty = request.POST.get('quantity')
            #get the item SOH from model table
            item_soh = Item_SOH.objects.get(item=pick_item)

            if int(item_soh.soh) < int(pick_qty):
                print("out of stock")
            else:
                #minus get item to soh
                new_soh = int(item_soh.soh) - int(pick_qty)
                #get the updated item soh
                item_soh.soh = new_soh
                item_soh.save()
                form.save()
                return redirect('home')
    else:
        form = ItemFormGet()
    context = {'form':form}
    return render(request,'inventory/get_item.html', context)

    