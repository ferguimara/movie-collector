from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from .models import Movie, Actor
from .forms import ReviewForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    review_form = ReviewForm()
    return render(request, 'movies/detail.html', {'movie': movie, 'review_form': review_form})

def add_review(request, movie_id):
    form=ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.movie_id = movie_id
        new_review.save()
    return redirect('detail', movie_id=movie_id)

class MovieCreate(CreateView):
    model=Movie
    fields = '__all__'

class MovieUpdate(UpdateView):
    model = Movie
    #restrict from updating certain fields
    fields = ['title', 'release_year', 'rating']

class MovieDelete(DeleteView):
    model = Movie
    success_url = '/movies/'

class ActorList(ListView):
  model = Actor

class ActorDetail(DetailView):
  model = Actor

class ActorCreate(CreateView):
  model = Actor
  fields = '__all__'

class ActorUpdate(UpdateView):
  model = Actor
  fields = ['name', 'birthday']

class ActorDelete(DeleteView):
  model = Actor
  success_url = '/actors/'