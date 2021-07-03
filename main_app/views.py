from django.shortcuts import render
from django.http import HttpResponse

#temporary data
class Movie:
    def __init__(self, title, release_year, rating):
        self.title = title,
        self.release_year = release_year,
        self.rating = rating,

movies = [
    Movie('Inception', 2010, 8.7)
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def movies_index(request):
    return render(request, 'movies/index.html', {'movies': movies})