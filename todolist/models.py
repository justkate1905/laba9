from django.db import models
from django.contrib.auth.models import User


class Tasklist(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name="user", default=0, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "#{}".format(self.name)


class Task(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    date_modified = models.DateField(auto_now=True)
    tasklist = models.ForeignKey(Tasklist, related_name='tasks', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    PRIORITY = (
        ('h', 'High'),
        ('m', 'Medium'),
        ('l', 'Low'),
        ('n', 'None')
    )

    priority = models.CharField(max_length=1, choices=PRIORITY, default='n')

    def __str__(self):
        return "{}".format(self.name)
