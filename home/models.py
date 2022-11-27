from datetime import date
from distutils.command.upload import upload
from unicodedata import name
from django.db import models
from datetime import datetime

# Create your models here.

class Destination(models.Model):

    name = models.CharField(max_length=100)
    place_code=models.CharField(max_length=3)
    tab_img = models.ImageField(upload_to='pics' , blank= True , null = True)
    img1 = models.ImageField(upload_to='pics' , blank= True , null = True)
    img2 = models.ImageField(upload_to='pics' ,  blank= True , null = True)
    img3 = models.ImageField(upload_to='pics' ,  blank= True , null = True)
    small_desc = models.TextField()
    breaf_desc = models.TextField()
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    


class Booking(models.Model):
    booking_id=  models.CharField(blank=True,null=True,max_length=40)
    place_name = models.CharField(max_length=100)
    place_code=models.CharField(max_length=3)
    booking_owner =  models.CharField(max_length=40)#owner username
    persons_name = models.TextField(blank=True , null = True)
    persons_adhar = models.TextField(blank=True , null = True)
    persons_gender = models.TextField(blank=True , null = True)
    persons_age= models.TextField(blank=True , null = True)
    count= models.CharField(max_length=5 ,default=0)
    slot= models.CharField(max_length=40)
    date= models.DateField(blank=True)


    def __str__(self):
        return self.booking_owner




class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
