from django.db import models


class Tasks(models.Model):
    message_id = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
