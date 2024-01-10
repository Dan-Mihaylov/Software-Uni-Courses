from django.db import models


class Task(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)


class Recommendation(models.Model):

    user_name = models.CharField(max_length=20)
    recommendation = models.TextField()


