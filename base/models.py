from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
  # many to one rel. between tasks and user (like referencing the user_id in tasks table)
  # CASCADE = when a user is deleted, all related tasks should be deleted as well
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField(max_length=255, null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  done = models.BooleanField(default=False)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['done']
