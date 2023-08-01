from django.http import JsonResponse
from django.shortcuts import render
from watchlist_app.models import Movie

# Create your views here.


def movie_list(request):
    """List all movies in the database"""
    movies = Movie.objects.all()
    return JsonResponse({'movies': list(movies.values())})


def movie_details(request, id):
    """Get a movie based on id"""
    movie = Movie.objects.get(pk=id)
    movie = {
        'name': movie.name,
        'description': movie.description,
        'id': movie.id,
        'active': movie.active
    }
    return JsonResponse({'movie': movie})
