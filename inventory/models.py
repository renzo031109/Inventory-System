from django.db import models

class ItemCode(models.Model):
    code = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.code
    

class ItemBase(models.Model):
    item_name = models.CharField(max_length=200, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    soh = models.IntegerField(null=True)
    item_code = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=50, null=True)

    
    class Meta:
        ordering = ["item_name"]

    def __str__(self):
        return self.item_code
    
    def totalValue(self):
        return self.soh * self.price
    

class Item(models.Model):
    item_code = models.ForeignKey(ItemCode, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True) 
    remarks = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return str(self.item_code)
    
    
    



      


    
    

    
    
        
