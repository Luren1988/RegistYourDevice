from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    device = models.ForeignKey('Device',on_delete=models.PROTECT)
    controller = models.ForeignKey('Controller',on_delete=models.PROTECT)
    sound =  models.ForeignKey('Sound',on_delete=models.PROTECT)
    memo = models.TextField()
    active = models.BooleanField()
    favorite = models.IntegerField()
    game = models.ForeignKey('GameTitle',on_delete=models.PROTECT,null=True)
    created = models.DateTimeField()
    modified =models.DateTimeField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.pk})

class Device(models.Model):
    name =models.CharField(max_length=50)
    price =models.IntegerField()
    company = models.ForeignKey('Company',on_delete=models.PROTECT)
    active = models.BooleanField()
    created = models.DateTimeField()
    modified =models.DateTimeField()

    def __str__(self):
        return self.name
    

class Controller(models.Model):
    name = models.CharField(max_length=50)
    price =models.IntegerField()
    company = models.ForeignKey('Company',on_delete=models.PROTECT)
    active = models.BooleanField()
    created = models.DateTimeField()
    modified =models.DateTimeField()
    def __str__(self):
        return self.name

class Sound(models.Model):
    name =models.CharField(max_length=50)
    price =models.IntegerField()
    company = models.ForeignKey('Company',on_delete=models.PROTECT)
    active = models.BooleanField()
    created = models.DateTimeField()
    modified =models.DateTimeField()
    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=20)

class GameTitle(models.Model):
    title = models.CharField(max_length=30)
    release_date = models.DateTimeField()

