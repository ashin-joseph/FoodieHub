from django.db import models

class fdCategoryDb(models.Model):
    c_name=models.CharField(max_length=50,null=True,blank=True)
    c_description=models.CharField(max_length=200,null=True,blank=True)
    c_picture=models.ImageField(null=True,blank=True)
class fbProductDb(models.Model):
    p_code=models.CharField(max_length=50,null=True,blank=True)
    p_category=models.CharField(max_length=50,null=True,blank=True)
    p_name=models.CharField(max_length=50,null=True,blank=True)
    p_price=models.IntegerField(null=True,blank=True)
    p_description=models.CharField(max_length=200,null=True,blank=True)
    p_picture=models.ImageField(null=True,blank=True)



