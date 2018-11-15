from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user}-{self.content}"