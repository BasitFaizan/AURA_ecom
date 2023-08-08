from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.

class users(BaseModel):
    username = models.CharField(name='Name', max_length=100)
    email = models.EmailField(name='Email',max_length=20,unique=True)
    password = models.CharField(name='password',max_length=20)
    

    def __str__(self):
        return self.username
    
class profile(BaseModel):
    mainUser = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    phoneNumber = models.IntegerField(name='Phonenumber',null=True,blank=True)
    profilePic = models.ImageField(name='profilePic',upload_to='media/profile',null=True,blank=True)
    fName = models.CharField(name='first_name',max_length=10,null=True,blank=True)
    lName = models.CharField(name='last_name',max_length=10,null=True,blank=True)
    gender = models.CharField(name='gender',max_length=10,null=True,blank=True)


class address(BaseModel):
    userAdd = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    userName = models.CharField(name='userName',null=True,blank=True,max_length=100)
    phoneNumber = models.IntegerField(name='phoneNumber',null=True,blank=True)
    pincode = models.IntegerField(name='pincode',null=True,blank=True)
    address = models.TextField(name='address',max_length=1000)
    state = models.CharField(name='state',max_length=100)
    alternateNumber = models.IntegerField(name='alternateNumber',null=True,blank=True)
    