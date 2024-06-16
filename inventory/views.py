from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Item, ItemBase, ItemCode
from .forms import ItemNewForm, ItemModelFormSet



# @login_required
def home(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request,'inventory/home.html', context)


# @login_required
# def add_item(request):
    
#     if request.method == 'POST':
#         form = ItemFormAdd(request.POST)
#         if form.is_valid(): 
#             #get the item name from the form
#             add_item = request.POST.get('item')
#             #get the item qty from the form
#             add_qty = request.POST.get('quantity')
#             #get the item SOH from model table

#             try:
#                 item_soh = ItemDetails.objects.get(id=add_item)
#                 print(item_soh)
#                 #compute add soh
#                 soh = int(item_soh.soh) + int(add_qty)
#                 #get the updated soh after add
#                 item_soh.soh = int(soh)
#                 #save tables
#                 item_soh.save()
#             except:
#                 item_soh = 0
#                 soh = int(item_soh) + int(add_qty)
            
#             form.save()
#             messages.success(request, "You added stock successfully!")
#             return redirect('home')
#     else:
#         form = ItemFormAdd()
#     context = {'form': form}
#     return render(request, 'inventory/add_item.html', context)


# @login_required
def delete_item(request, id):
    if request.method == 'POST':
        item = Item.objects.get(id=id)
        item_soh = Item.objects.get(item_name=item.item)

        updated_soh = int(item_soh.soh) + int(item.quantity)
        item_soh.soh = updated_soh
        item_soh.save()
        item.delete()
    return redirect('home')



def summary_item(request):
    items = ItemBase.objects.all()
    context = {'items': items}
    return render(request, 'inventory/summary.html', context)



def get_item(request):
    
    if request.method == 'POST':
        formset = ItemModelFormSet(request.POST)    
        if formset.is_valid():
            for form in formset:

                if form.cleaned_data.get('item_code'):

                    itemGetForm = form.save(commit=False)
                    itemGetForm.remarks = "OUT"

                    #get the item name from the form
                    get_item_code = form.cleaned_data.get('item_code')
                    #get the item qty from the form
                    get_qty = form.cleaned_data.get('quantity')
                    #get the item SOH from model table
                    item_soh = ItemBase.objects.get(item_code=get_item_code)
                    print(get_item_code)
                    print(get_qty)
                    print(item_soh)

                    if int(item_soh.soh) < int(get_qty):
                        print("out of stock")
                        messages.error(request, f"Sorry, Your available stock for {item_soh.item_name} is only {item_soh.soh}")
                    else:
                        #minus get item to soh
                        new_soh = int(item_soh.soh) - int(get_qty)
                        #get the updated item soh
                        item_soh.soh = new_soh
                        item_soh.save()
                        form.save()
                        messages.success(request, "You deducted the item from the records")
                        return redirect('home')
    else:
        formset = ItemModelFormSet(queryset=Item.objects.none())
    context = {'formset':formset}
    return render(request,'inventory/get_item.html', context)


def new_item(request):

    if request.method == 'POST':
        form = ItemNewForm(request.POST)

        if form.is_valid():
            #get the value of the form
            form_item_name = request.POST.get('item_name')
            form_item_brand = request.POST.get('brand_name')
            form_item_soh= request.POST.get('soh')
                     
            #using try-except method in case of null value
            try:
                record_name = ItemBase.objects.filter(item_name=form_item_name, brand_name=form_item_brand)

                for record in record_name:
                    if record.item_name == form_item_name and record.brand_name == form_item_brand:
                        messages.error(request, "Item already exist!")
                        return redirect('new_item')
                       
            except:
                record_name = None

            #assign default value to remarks
            concat = form_item_name + " | " + form_item_brand
            itemcode = ItemCode(code=concat)
            itemcode.save()

            #Assign form to a variable
            itemAddForm = form.save(commit=False)    
     
            #assign generated code value to itemcode 
            itemAddForm.item_code = concat

            itemAddForm.save()

            messages.success(request, "New Item added successfully!")
            return redirect('summary_item')
    else:
        form = ItemNewForm()

    context = {'form': form}
    return render(request, 'inventory/new_item.html', context)


def add_item(request):

    if request.method == 'POST':
        formset = ItemModelFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                # #this is just for checking of form submitted
                # for a,b in form.cleaned_data.items():
                #     print(a,b)
                
                # only save if name is present
                print(form.cleaned_data.get('item_code'))
                print(form.cleaned_data.get('quantity'))
                if form.cleaned_data.get('item_code'):  
                    #assign default value to remarks 
                    itemAddForm = form.save(commit=False)    
                    itemAddForm.remarks = "IN"

                    #get the item name from the form 
                    add_item_code = form.cleaned_data.get('item_code')
                    #get the item qty from the form
                    add_qty = form.cleaned_data.get('quantity')
                    #get the item SOH from model table


                    try:
                        item_soh = ItemBase.objects.get(item_code=add_item_code)
                        print(f'try this item soh = {item_soh}')
                        #compute add soh
                        soh = int(item_soh.soh) + int(add_qty)
                        #get the updated soh after add
                        item_soh.soh = int(soh)
                        #save tables
                        item_soh.save()
                    except:
                        item_soh = 0
                        soh = int(item_soh) + int(add_qty)

                    itemAddForm.save()
            messages.success(request, "You added stock successfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Input!")

    else:
        formset = ItemModelFormSet(queryset=Item.objects.none())

    context = {'formset': formset}
    return render(request, 'inventory/add_item.html', context)

