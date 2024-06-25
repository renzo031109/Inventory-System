from typing import Any
from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item, ItemBase, ItemCode
from .forms import ItemNewForm, ItemModelFormSet
from .filters import ItemFilter, ItemBaseFilter
from django.http import HttpResponse
from openpyxl import Workbook



@login_required
def home(request):
    
    items = Item.objects.all()
    # item_count_total= items.count()

    itemFilter = ItemFilter(request.GET, queryset=items)
    items = itemFilter.qs
    
    item_count = items.count()
    
    if item_count > 0 :
        messages.info(request, f"Found '{item_count}' item(s) in the database")
    else:
        messages.info(request, f"Item not Found in the database ")

    context = {
        'items': items, 
        'item_count': item_count, 
        'itemFilter': itemFilter
        }
    return render(request,'inventory/home.html', context)


@login_required
def delete_item(request, id):
    if request.method == 'POST':
        #get the selected value
        item = Item.objects.get(id=id)
        item_soh = ItemBase.objects.get(item_code=item.item_code)

        #return the quantity of the deleted item
        updated_soh = int(item_soh.soh) + int(item.quantity)
        item_soh.soh = updated_soh

        #update Total value and save
        total = updated_soh * item_soh.price
        item_soh.total_value = total
        item_soh.save()
        item.delete()
        messages.success(request, "Item is deleted successfully")
    return redirect('home')


@login_required
def summary_item(request):
    items = ItemBase.objects.all()
    # item_count_total= items.count()

    itemFilter = ItemBaseFilter(request.GET, queryset=items)
    items = itemFilter.qs
    item_count = items.count()

    if item_count > 0 :
        messages.info(request, f"Found '{item_count}' item(s) in the database")
    else:
        messages.info(request, f"Item not Found in the database ")

    context = {
        'items': items,
        'item_count': item_count,
        'itemFilter': itemFilter
        }
    return render(request, 'inventory/summary.html', context)


@login_required
def new_item(request):

    if request.method == 'POST':
        form = ItemNewForm(request.POST)

        if form.is_valid():
            #get the value of the form
            form_item_name = request.POST.get('item_name')
            form_item_brand = request.POST.get('brand_name')
            form_item_soh = request.POST.get('soh')
            form_item_uom = request.POST.get('uom')
                     
            #using try-except method in case of null value
            try:
                record_name = ItemBase.objects.filter(item_name=form_item_name, brand_name=form_item_brand)

                for record in record_name:
                    if record.item_name.upper() == form_item_name.upper() and record.brand_name.upper() == form_item_brand.upper():
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

            #define user for the staffname
            user = request.user

            #copy newitem to Item Transaction
            itemTransaction = Item(item_name=form_item_name, brand_name=form_item_brand, quantity=form_item_soh, remarks="BEGINNING",uom=form_item_uom, staff_name=user.username)
            itemTransaction.save()

            #assign generated code value to itemcode 
            itemAddForm.item_code = concat
            itemAddForm.save()

            messages.success(request, "New Item added successfully!")
            return redirect('summary_item')
    else:
        form = ItemNewForm()

    context = {'form': form}
    return render(request, 'inventory/new_item.html', context)


@login_required
def add_item(request):

    if request.method == 'POST':
        formset = ItemModelFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                # #this is just for checking of form submitted
                # for a,b in form.cleaned_data.items():
                #     print(a,b)
                
                # check if itemcode is selected
                if form.cleaned_data.get('item_code'):  
                    
                    #get the item name from the form 
                    add_item_code = form.cleaned_data.get('item_code')
                    #get the item qty from the form
                    add_qty = form.cleaned_data.get('quantity')
                    
                    
                    try:
                        #get the item SOH from model table
                        item_soh = ItemBase.objects.get(item_code=add_item_code)
    
                        #compute add soh
                        soh = int(item_soh.soh) + int(add_qty)
                        #get the updated soh after add
                        item_soh.soh = int(soh)

                        #update Total value
                        total = item_soh.soh * item_soh.price
                        item_soh.total_value = total

                        #save tables
                        item_soh.save()
                    except:
                        item_soh = 0
                        soh = int(item_soh) + int(add_qty)

                    #assign default values  
                    itemAddForm = form.save(commit=False)    
                    itemAddForm.remarks = "IN"
                    itemAddForm.item_name = item_soh.item_name
                    itemAddForm.brand_name = item_soh.brand_name
                    itemAddForm.uom = item_soh.uom
                    #get the current user
                    user = request.user
                    itemAddForm.staff_name = user.username
                    # itemAddForm.client_name = "SHORE360"
                    # itemAddForm.department_name = "PURCHASING"
                    itemAddForm.save()
                    
            messages.success(request, "You added stock successfully!")
            
            return redirect('home')
        else:
            messages.error(request, "Invalid Input!")

    else:
        formset = ItemModelFormSet(queryset=Item.objects.none())

    context = {'formset': formset}
    return render(request, 'inventory/add_item.html', context)


@login_required
def get_item(request):

    #Initiate a list variable for the input select fields
    staff_name_list = []
    client_name_list = []
    department_name_list = []

    #list for validation checking
    item_error_list = []
    item_success_list = []

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
                    
                    #get the item name from the form 
                    get_item_code = form.cleaned_data.get('item_code')

                    #get the item qty from the form
                    get_qty = form.cleaned_data.get('quantity')

                    #get the item SOH from model table       
                    item_soh = ItemBase.objects.get(item_code=get_item_code)

                    #get the staff name values
                    get_staff_name = form.cleaned_data.get('staff_name')
                    get_client_name = form.cleaned_data.get('client_name')
                    get_department_name = form.cleaned_data.get('department_name')

                    #populate the list from the user input
                    staff_name_list.append(get_staff_name)
                    client_name_list.append(get_client_name)
                    department_name_list.append(get_department_name)
                    
                    #get the first value of the form
                    staff_name = staff_name_list[0]
                    client_name = client_name_list[0]
                    department_name = department_name_list[0]

                    if item_soh.soh < get_qty:
                        messages.error(request, f"Ooops, Your available stock for '{item_soh.item_name}' is only '{item_soh.soh}")
                        item_error_list.append(item_soh.item_name)
                    else:
                        item_success_list.append(item_soh.item_name)
                        #compute add soh
                        soh = int(item_soh.soh) - int(get_qty)
                        #get the updated soh after add
                        item_soh.soh = int(soh)
                        #update Total value
                        total = item_soh.soh * item_soh.price
                        item_soh.total_value = total
                        #save tables
                        item_soh.save()

                        #assign default value to remarks 
                        itemGetForm = form.save(commit=False)    
                        itemGetForm.remarks = "OUT"
                        itemGetForm.item_name = item_soh.item_name
                        itemGetForm.brand_name = item_soh.brand_name
                        itemGetForm.uom = item_soh.uom
                        itemGetForm.staff_name = staff_name
                        itemGetForm.client_name = client_name
                        itemGetForm.department_name = department_name
                        itemGetForm.save()
                        
            #assign length variables
            invalid_form = len(item_error_list)
            valid_form = len(item_success_list)

            # if values are valid send to submitted template
            if invalid_form == 0 and valid_form != 0:
                return redirect('submitted')

            # if 1 of the values are valid 
            elif invalid_form > 0 and valid_form > 0:
                messages.info(request, f"{valid_form} item(s) are submitted. Please re-input the item(s) with insufficient stock on hand.")
                return redirect('get_item')    
            # re input the items     
            else:
                return redirect('get_item')
            
        else:
            messages.error(request, "Invalid Input!")

    else:
        formset = ItemModelFormSet(queryset=Item.objects.none())

    context = {'formset': formset}
    return render(request, 'inventory/get_item.html', context)


def submitted(request):
    return render(request, 'inventory/submitted.html')


def export_excel(request):

    #Export excel function
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="inventory_report.xlsx"'

    # Declare Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Inventory Report"

    # Add headers
    headers =   [
                'ITEM NAME',	
                'BRAND NAME',
                'QUANTITY',	
                'UOM',	
                # 'DATE ADDED',
                'REMARKS',	
                'STAFF NAME',
                # 'CLIENT NAME',
                'DEPARTMENT NAME'	
                ]
    
    ws.append(headers)

    # Add data from the model
    items = Item.objects.all()
    for item in items:
        ws.append([
            item.item_name,
            item.brand_name,
            item.quantity,
            item.uom,
            # item.date_added,
            item.remarks,
            item.staff_name,
            # item.client_name,
            # item.department_name
        ])
    
    wb.save(response)
    return response

