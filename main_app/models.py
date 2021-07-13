from django.db import models
from django.urls import reverse

SCORE = (
    ('A', 'Excelent'),
    ('B', 'Good'),
    ('C', 'Okay'),
    ('D', 'Bad'),
    ('F', 'Terrible'),
)
# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=250)
    birthday = models.DateField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('actors_detail', kwargs={'pk': self.id})

class Movie(models.Model):
    title = models.CharField(max_length=100, default='hello')
    release_year = models.CharField(max_length=4, default=2000)
    rating = models.FloatField(default=5.0)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id })

class Review(models.Model):
    date = models.DateField()
    review = models.TextField(max_length=1000)
    score = models.CharField(
        max_length=1,
        choices=SCORE,
        default=SCORE[0][0]
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.score