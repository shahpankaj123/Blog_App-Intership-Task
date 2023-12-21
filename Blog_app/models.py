from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    desc=models.TextField()
    img=models.ImageField(upload_to='Blog_img/')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
