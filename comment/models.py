from django.db import models
from blog.models import Post

class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    url= models.URLField(null=True)
    content = models.TextField()
    time = models.DateTimeField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)

