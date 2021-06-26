from django.db import models

# Create your models here.
class Carousel(models.Model):
    headings = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=200,null=True)
    img = models.ImageField(upload_to='img/carousel',null=True)
    submitted_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)  

    class Meta:
        db_table :'Carousel'

class Services(models.Model):
    title = models.CharField(max_length=50,null=True)
    content = models.CharField(max_length=200,null=True) 
    gif= models.ImageField(upload_to='img/services',null=True)

    class Meta:
        db_table:'Services'

class Client(models.Model):
    link = models.CharField(max_length=300,null=True)
    logo = models.ImageField(upload_to='img/client',null=True)

    class Meta:
        db_table:'Client'

class About(models.Model):
    desc1=models.CharField(max_length=300,null=True)
    desc2=models.CharField(max_length=300,null=True)
    desc3=models.CharField(max_length=300,null=True)
    img = models.ImageField(upload_to='img/about',null=True)

    class Meta:
        db_table:'About'

    def __str__(self):
        return self.desc1 + " " + self.desc2 + " " + self.desc3
