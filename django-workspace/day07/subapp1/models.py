from django.db import models

# Create your models here.

class Member(models.Model):
    name = models.CharField(max_length = 30)    # 짧은 글자로 구성된 데이터
    age = models.IntegerField()                 # 정수로 구성된 데이터

class Account(models.Model):
    userid = models.CharField(max_length = 20)
    userpw = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    