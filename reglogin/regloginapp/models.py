from django.db import models

class Registration(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    mobile=models.BigIntegerField()


