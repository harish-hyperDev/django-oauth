from django.db import models


# Create your models here.
class Posts(models.Model):
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