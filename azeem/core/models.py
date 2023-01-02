from email.headerregistry import Address
from tokenize import Name
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class StratContract1(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    file = models.FileField(blank=True, null=True,upload_to='documents/',default=False)
    desc=models.TextField()
    price=models.FloatField()
    phone=models.CharField(max_length=100)

   
    def __str__(self):
        return self.name

class Contact(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField( max_length=120)
    email=models.EmailField(max_length=120)
    phone=models.CharField(max_length=120)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name



class Employee(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    designation=models.CharField(max_length=100)
    phone=models.CharField( max_length=50)
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name
     
class Route_From(models.Model):
    route_from=models.CharField(max_length=100)

    def __str__(self):
        return self.route_from

class Route_To(models.Model):
    route_to=models.CharField(max_length=100)

    def __str__(self):
        return self.route_to





class Tourism(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    expected_rate=models.FloatField()
    route_from=models.ForeignKey(Route_From,on_delete=models.CASCADE)
    route_to=models.ForeignKey(Route_To,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Tourism_Apply_Form(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    phone=models.CharField( max_length=50)
    travel_date=models.CharField(max_length=40)
    persons = models.CharField(max_length=120)
    from_route=models.ForeignKey(Route_From,on_delete=models.CASCADE)
    to_route=models.ForeignKey(Route_To,on_delete=models.CASCADE)
    adult=models.CharField(max_length=100)
    child=models.CharField(max_length=100)

    def __str__(self):
        return self.name
