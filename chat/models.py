from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=50)
    content = models.TextField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} at {self.timestamp}"