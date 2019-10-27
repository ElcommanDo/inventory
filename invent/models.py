from django.db import models

# Create your models here.
class Device(models.Model):
    choices = (('Available','item ready to be prushase'),('Sold','item has been sold'),('restoking','item is restoking in few days'))
    type = models.CharField(max_length=120,blank=False)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
    status = models.CharField(max_length=15,blank=False,choices=choices,default = 'Available')
    issue = models.CharField(max_length = 100,default='No Issues')

    class Meta:
        abstract = True
    
    def __str__(self):
        return ' type : {}'.format(self.type)

class Laptop(Device):
    image = models.ImageField(upload_to='Laptops_pic')
    name_of_class = models.CharField(max_length=20,default='Laptop',blank=True,null=True)

    def __str__(self):
        return ' laptop type : {}'.format(self.type)


class Mobile(Device):
    
    image = models.ImageField(upload_to='mobiles_pic')
    name_of_class = models.CharField(max_length=20,default='Desktop',blank=True,null=True)

    def __str__(self):
        return ' mobile type : {}'.format(self.type)


class Desktop (Device):
    
    image = models.ImageField(upload_to='desktop_pic')
    name_of_class = models.CharField(max_length=20,default='Mobile',blank=True,null=True)

    def __str__(self):
        return ' desktop type : {}'.format(self.type)

