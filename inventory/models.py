from django.db import models


class ItemBase(models.Model):
    item_name = models.CharField(max_length=200, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    soh = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=200, null=True)
    
    class Meta:
        ordering = ["item_name"]

    def __str__(self):
        return self.item_name
    

class Item(ItemBase):
    item_code = models.ForeignKey(ItemBase, related_name='code', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True) 
    remarks = models.CharField(max_length=50, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    


    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return str(self.item_name)


# class ItemPrice(ItemBase): 
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     date_added = models.DateTimeField(auto_now_add=True)
    

#     def __str__(self):
#         return self.item_name

      


    
    

    
    
        
