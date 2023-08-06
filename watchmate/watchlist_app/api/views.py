#!/usr/bin/python3
"""Define Views for movie RESFUL API DEFAULT RESPONSE"""
from rest_framework.exceptions import status
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializers


class MovieListAV(APIView):
    """Class View of movies list """

    def get(self, request):
        """Returns all movies in the movie tables"""
        movies = Movie.objects.all()
        movies_data = MovieSerializers(movies, many=True).data
        return Response(movies_data)

    def post(self, request):
        """ Post a request to db"""
        movie = MovieSerializers(data=request.data)
        if movie.is_valid():
            movie.save()
            return Response(movie.data)
        else:
            return Response(movie.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAV(APIView):
    """Find the details of a particular movie by id"""

    def get(self, request, id):
        """Get a single movie identified by an id"""
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response({"error": "Not found"},
                            status=status.HTTP_404_NOT_FOUND)
        movie_data = MovieSerializers(movie).data
        return Response(movie_data, status=status.HTTP_200_OK)

    def put(self, request, id):
        """Takes an id and put the required data in the right movie"""
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response({"error": "Not found"},
                            status=status.HTTP_404_NOT_FOUND)
        movie_data = MovieSerializers(movie, data=request.data)
        if movie_data.is_valid():
            movie_data.save()
            return Response(movie_data.data, status=status.HTTP_200_OK)
        else:
            return Response(movie_data.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        """Delete a movie from db"""
        try:
            movie = Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            return Response({'error': "Not found"},
                            status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response({}, status=status.HTTP_200_OK)
