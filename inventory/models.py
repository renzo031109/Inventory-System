from django.db import models




class ItemCode(models.Model):
    code = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.code
    
    def save(self):
        self.code= self.code.upper()
        super(ItemCode, self).save()
    

class UOM(models.Model):
    uom = models.CharField(max_length=30)
    
    def __str__(self):
        return self.uom
    
    class Meta:
        ordering = ["uom"]

class ItemBase(models.Model):
    item_name = models.CharField(max_length=200, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    soh = models.IntegerField(null=True)
    item_code = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=50, null=True)
    uom = models.ForeignKey(UOM, on_delete=models.CASCADE, null=True)

    
    class Meta:
        ordering = ["item_name"]

    def __str__(self):
        return self.item_code
    
    #save input to uppercase
    def save(self):
        self.item_name = self.item_name.upper()
        self.brand_name = self.brand_name.upper()
        self.item_code = self.item_code.upper()
        super(ItemBase, self).save()
        
    #computation of total price per item
    def totalValue(self):
        return self.soh * self.price
    

class Item(models.Model):
    item_code = models.ForeignKey(ItemCode, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True) 
    remarks = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    uom = models.CharField(max_length=20, null=True)
    item_name = models.CharField(max_length=200, blank=True, null=True, )
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return str(self.item_name)
    
    def save(self):
        self.item_name = self.item_name.upper()
        self.brand_name = self.brand_name.upper()
        super(Item, self).save()
    
    def sort_ascending(self):
        return self.date_added.order_by('')

    @property
    def sorted_attendee_set(self):
        return self.date_added.order_by('date_added')
    
    @property
    def sorted_attendee_set(self):
        return self.date_added.order_by('-date_added')
    
    



      


    
    

    
    
        
