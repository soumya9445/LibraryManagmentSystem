from django.db import models

# Create your models here.
class Admin(models.Model):
    #id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=70)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=70)
    photo=models.ImageField(upload_to='admin_images/',default=False)
class Library(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    books=models.FileField(upload_to='books_images/',max_length=1000)
