from typing import overload
from django.db import models
from datetime import datetime
# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.TimeField(default= datetime.now(), blank=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural= "Posts"