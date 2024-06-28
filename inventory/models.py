from django.db import models


class Client(models.Model):
    client = models.CharField(max_length=200)

    def __str__(self):
        return self.client
    
    def save(self):
        self.client = self.client.upper()
        super(Client, self).save()


class Department(models.Model):
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.department

    def save(self):
        self.department = self.department.upper()
        super(Department, self).save()


class ItemCode(models.Model):
    code = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ["code"]
    
    def save(self):
        self.code = self.code.upper()
        super(ItemCode, self).save()
    

class UOM(models.Model):
    uom = models.CharField(max_length=30)
    
    def __str__(self):
        return self.uom
    
    class Meta:
        ordering = ["uom"]

    def save(self):
        self.uom= self.uom.upper()
        super(UOM, self).save()


class ItemBase(models.Model):
    item_name = models.CharField(max_length=200, null=True)
    brand_name = models.CharField(max_length=200, null=True)
    soh = models.IntegerField(null=True)
    item_code = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
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
        
    # #computation of total price per item
    # def totalValue(self):
    #     return self.soh * self.price
    

class Item(models.Model):
    item_code = models.ForeignKey(ItemCode, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True) 
    remarks = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    uom = models.CharField(max_length=20, null=True)
    item_name = models.CharField(max_length=200, blank=True, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    staff_name = models.CharField(max_length=100, null=True, blank=True)
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    
    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return str(self.item_name)
    
    def save(self):
        self.item_name = self.item_name.upper()
        self.brand_name = self.brand_name.upper()
        super(Item, self).save()
    



    
    



      


    
    

    
    
        
