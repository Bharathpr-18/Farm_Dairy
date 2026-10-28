from django.db import models

# Create your models here.
class student(models.Model):
    sid = models.CharField(max_length=3)
    sname = models.CharField(max_length=23)
