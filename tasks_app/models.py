from django.db import models

# Create your models here.

# Users class
class User(models.Model):
    username = models.CharField(max_length = 25, unique = True)
    password = models.CharField(max_length = 40)

    def __str__(self):
        return self.username

# Tasks class
class Task(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 85)
    deadline = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'tasks')

    def __str__(self):
        return str(f"{self.user}: {self.name}")