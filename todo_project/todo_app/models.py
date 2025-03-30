from django.db import models

# Create your models here.
#This is where i find the structure of our tasks in the database

class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.description