from django.db import models


class ItemName(models.Model):
    item_name = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200)
    uom = models.CharField(max_length=20)

    def __str__(self):
        return self.item_name

class Item(models.Model):
    item = models.ForeignKey(ItemName, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item
    
    
    
    
        
