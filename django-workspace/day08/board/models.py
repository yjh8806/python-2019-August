from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 50)
    writer = models.CharField(max_length = 20)  # 짧은 글 : CharField
    time = models.DateField(auto_now=True)      # 자동으로 현재 시간을 기록하게 설정
    text = models.TextField(max_length = 1000)  # 긴 글 : TextField