from django.db import models

# Create your models here.

class Member(models.Model):
    userid = models.CharField(max_length = 20)
    userpw = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    age = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 20)