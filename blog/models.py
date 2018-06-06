from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

class Tag(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    time = models.DateTimeField()




