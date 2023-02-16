from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    due_date = models.DateField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             )
