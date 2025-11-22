from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

# Users class
class User(models.Model):
    username = models.CharField(max_length = 25, unique = True)
    password = models.CharField(max_length = 128)
    
    def __str__(self):
        return self.username
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw):
        return check_password(raw, self.password)
    
    def set_username(self, new_username):
        self.username = new_username

    def get_username(self):
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
    
