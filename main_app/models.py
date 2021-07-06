from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100),
    release_year = models.CharField(),
    rating = models.FloatField(),

    def __str__(self):
        return self.title