from django.db import models
from django.contrib.auth.models import User


#
class Product(models.Model):
   CAT=((1,'book'),(2,'Jewellery'),(3,'Clothes'))
   name=models.CharField( max_length=500)
   country=models.CharField( max_length=50)
   event=models.CharField( max_length=50)
   cat=models.IntegerField(verbose_name='Catagory',choices=CAT,default=1)
   pdetails=models.CharField(max_length=200)
   is_active=models.BooleanField(default=True)
   pimage=models.ImageField(upload_to='image',default=True)
   pimage_a=models.ImageField(upload_to='images',default=True)
   pimage_b=models.ImageField(upload_to='images',default=True)
   pimage_c=models.ImageField(upload_to='images',default=True)
   pimage_d=models.ImageField(upload_to='images',default=True)
   
class Image(models.Model):
   pimage=models.ImageField(upload_to='image',default=True)
   pimage_1=models.ImageField(upload_to='images',default=True)
   pimage_2=models.ImageField(upload_to='images',default=True)
   pimage_3=models.ImageField(upload_to='images',default=True)
   pimage_4=models.ImageField(upload_to='images',default=True)
   

#class Cart(models.Model):
   #uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')
  # pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')

   
   
   
   
   
   
