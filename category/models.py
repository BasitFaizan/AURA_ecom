from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.

class category(BaseModel):
    # categoryId = models.AutoField(primary_key=True)
    categoryName =  models.CharField(name='categoryName', max_length=100)
    productImg = models.ImageField(name='productImg',upload_to='media/product',null=True,blank=True)
    def __str__(self)-> str:
        return self.categoryName
    
class product(BaseModel):
    userProduct = models.ForeignKey(User,on_delete=models.CASCADE,related_name='userProduct')
    categoryName = models.ForeignKey(category,on_delete=models.CASCADE,related_name='category')
    subCategory = models.CharField(name='subCategory',max_length=20)
    productName = models.CharField(name='productName',max_length=20)
    productDescription = models.TextField(name='productDescription',max_length=100)
    productPrice = models.CharField(name='productPrice',max_length=10,null=True,blank=True)
    productRatings = models.CharField(name='productRatings',max_length=10)
    prod_img_1 = models.ImageField(name='prod_img_1',upload_to='media/productImage')
    prod_img_2 = models.ImageField(name='prod_img_2',upload_to='media/productImage')
    prod_img_3 = models.ImageField(name='prod_img_3',upload_to='media/productImage')