from django.db import models


class ItemName(models.Model):
    item_name = models.CharField(max_length=200, null=True,)
    brand_name = models.CharField(max_length=200, null=True,)

    class Meta:
        verbose_name_plural = 'Item Name'
        ordering = ["item_name"]

    def __str__(self):
        return self.item_name
    

class Item(models.Model):
    item = models.ForeignKey(ItemName, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField() 
    remarks = models.CharField(max_length=50, null=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Item'

    def __str__(self):
        return str(self.item)
    
    
class Item_SOH(models.Model):
    item = models.ForeignKey(ItemName, null=True, on_delete=models.CASCADE)
    soh = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Item SOH'
    
    def __str__(self):
        return f'{str(self.item)} = {str(self.soh)}'
    
    
    
        
