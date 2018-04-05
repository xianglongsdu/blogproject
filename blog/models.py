from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    created_time = models.DateTimeField(verbose_name='创建日期')
    modified_time = models.DateTimeField(verbose_name='修改日期')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
        




