import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    deadline = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # one to many relationship

    # between user and task where task can have only one user while user can have many tasks
    # on_delete=models.CASCADE : when user deleted , already tasks will be deleted

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
