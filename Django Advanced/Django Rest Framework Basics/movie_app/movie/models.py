from django.db import models


class Director(models.Model):

    name = models.CharField(max_length=100)


class Movie(models.Model):

    title = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.year}'
