from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)  # 제목
    completed = models.BooleanField(default=False)  # 완료여부
