from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
#Моделька для создания постов в БД
class Post(models.Model):
  title = models.CharField(max_length=120)
  content = models.TextField()
  published_at = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
