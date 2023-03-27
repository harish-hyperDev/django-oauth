from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loggedin_user", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PostItem(models.Model):
    category = models.ForeignKey(Posts, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=70)
    image = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.title

    def __value__(self):
        return self.category
