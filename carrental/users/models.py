from django.db import models
import datetime

# Create your models here.
class Cardetails(models.Model):
    carimage = models.ImageField(null=True, blank=True, upload_to="images/", default="")
    carimagefront = models.ImageField(null=True, blank=True, upload_to="images/", default="")
    carimageback = models.ImageField(null=True, blank=True, upload_to="images/", default="")
    carimageleft = models.ImageField(null=True, blank=True, upload_to="images/", default="")
    carimageright = models.ImageField(null=True, blank=True, upload_to="images/", default="")
    carno=models.CharField(max_length=15,default=0)
    ownermobileno=models.IntegerField(max_length=100,default="None")
    carcolor=models.CharField(max_length=100,default="None")
    seatingcapacity=models.IntegerField(max_length=15,default=0)
    onrent=models.CharField(max_length=100,default="No")
    carmodel=models.IntegerField(max_length=15,default=0)
    carcompany=models.CharField(max_length=100,default="XYZ")
    cartype=models.CharField(max_length=100,default="Petrol/Diesel")
    cargears=models.CharField(max_length=100, default="Automatic/Gear")
    priceperday=models.IntegerField(max_length=15,default=0)
    rentedto=models.CharField(max_length=100,default="XYZ")
    fromm=models.DateField(default=datetime.date.today)
    to=models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.carno

