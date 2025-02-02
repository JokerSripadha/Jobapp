from django.db import models
from django.utils.text import slugify

# Create your models here.
class Location(models.Model):
    street=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
    
    def __str__(self):
        return self.city


class Author(models.Model):
    name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Skills(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
class JobPost(models.Model):
    job_type=[
        ('Full Time', 'Full Time'),
        ('Part Time','Part Time')
    ]
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    expiry=models.DateField(null=True)
    salary=models.IntegerField()
    slug=models.SlugField(null=True,max_length=40,unique=True)
    location=models.OneToOneField(Location,on_delete=models.CASCADE,null=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    skills=models.ManyToManyField(Skills)
    type=models.CharField(max_length=200, null=False,choices=job_type)
    
    def save(self,*args,**kwargs):
        if not self.id :
            self.slug =slugify(self.title)
        return super(JobPost,self).save(*args,**kwargs)
    
    
    def __str__(self):
        return self.title
    
    
    
