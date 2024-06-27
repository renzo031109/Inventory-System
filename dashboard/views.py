from django.shortcuts import render
from inventory.models import Item, ItemBase
import datetime

# Create your views here.
def dashboard_view(request):

    #initialize critical value
    critical_value = 10

    itembase = ItemBase.objects.all()
    item = Item.objects.all()

    #Total Item Count
    item_count = itembase.count()

    #Total Items with critical stocks
    critical_count = 0
    for critical in itembase:
        if critical.soh <= critical_value:
            critical_count += 1

    #Transaction today
    transaction_count = 0
    for transaction_date in item:
        if transaction_date.date_added.date() == datetime.datetime.now().date():
            transaction_count += 1
            

    context = {
        'item_count': item_count,
        'critical_count': critical_count,
        'itembase': itembase,
        'transaction_count': transaction_count

    }

    return render(request, 'dashboard/dashboard_template.html', context)