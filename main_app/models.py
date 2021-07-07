from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, default='hello')
    release_year = models.CharField(max_length=4, default=2000)
    rating = models.FloatField(default=5.0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id })