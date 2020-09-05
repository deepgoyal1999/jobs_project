from django.db import models

# Create your models here.
class delhijobinfo(models.Model):
    date=models.DateField();
    cname=models.CharField(max_length=30);
    title=models.CharField(max_length=30);
    phonenum=models.IntegerField();

class hydjobinfo(models.Model):
    date=models.DateField();
    cname=models.CharField(max_length=30);
    title=models.CharField(max_length=30);
    phonenum=models.IntegerField();


class mumbaijobinfo(models.Model):
    date=models.DateField();
    cname=models.CharField(max_length=30);
    title=models.CharField(max_length=30);
    phonenum=models.IntegerField();
