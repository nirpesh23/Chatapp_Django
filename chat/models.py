from concurrent.futures import thread
from django.db import models

class ChatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, max_length=50)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message 