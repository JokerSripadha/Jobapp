from django.db import models

# Create your models here.
class UploadImage(models.Model):
    Image=models.ImageField(upload_to='images')
    description=models.CharField(max_length=200)
    
