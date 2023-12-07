from django.db import models
from django.conf import settings

class Post(models.Model):
    Title = models.CharField(max_length=255)
    Content = models.TextField()
    Category = models.CharField(max_length=100)
    Date_Published = models.DateField()

    def __str__(self):
        return f"{self.Title}"


class Comment(models.Model):
    Post_ID = models.ForeignKey(Post, on_delete=models.CASCADE)
    User_ID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, to_field='username')
    Content = models.TextField()
    Date_Posted = models.DateTimeField()
    def __str__(self):
        return f"{self.Post_ID}"

class Category(models.Model):
    Name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Name}"


