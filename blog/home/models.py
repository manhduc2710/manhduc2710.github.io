from django.db import models

# Create your models here.
class Post(models.Model):
    ten = models.CharField(max_length=100)
    anh = models.ImageField()
    noidung = models.TextField(default='')
    thoigian = models.DateField(auto_now_add=True)