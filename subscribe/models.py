from django.db import models


New_letters=[
    ('W','Weekly'),
    ('M','Monthly')
]
# Create your models here.
class Subscribe(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    option=models.CharField(max_length=2,choices=New_letters)
    
    
    def __str__(self):
        return self.email
