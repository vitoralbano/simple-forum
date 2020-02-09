from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=255)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', null=True, on_delete=models.SET_NULL)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
