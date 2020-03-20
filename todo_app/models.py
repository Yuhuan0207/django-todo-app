from django.db import models

class Task(models.Model):

    task_name = models.CharField(max_length = 200)
    task_priority = models.CharField(max_length = 200)

    def __str__(self):
        return self.task_name
