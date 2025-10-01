from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)        # 本のタイトル
    author = models.CharField(max_length=100)       # 著者
    genre = models.CharField(max_length=100)        # ジャンル
    description = models.TextField(blank=True)      # 説明（空でもOK）

    def __str__(self):
        return self.title
