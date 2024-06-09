from django.db import models


class ItemDetails(models.Model):
    item_name = models.CharField(max_length=200, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    soh = models.IntegerField(null=True)

    class Meta:
        db_table = 'item'
        verbose_name_plural = 'Item Name'
        ordering = ["item_name"]

    def __str__(self):
        return self.item_name
    

class Item(models.Model):
    item = models.ForeignKey(ItemDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField() 
    remarks = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Item'
        ordering = ["-date_added"]

    def __str__(self):
        return str(self.item)
    
    

    
    
        
