from django.db import models

# Create your models here.


class UserRegister(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=25)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    locality = models.CharField(max_length=20)
    status =models.CharField(max_length=15)
    
    def __str__(self):
        return self.name            
    
    
class image_uoload(models.Model):
    image=models.ImageField(upload_to='media/')
    
    
    def __str__(self):
        return self.image.name
     

                                                                        