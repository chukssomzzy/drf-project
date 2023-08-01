from django.urls import include, path

from watchlist_app.views import movie_list, movie_details


urlpatterns = [
    path('list/', movie_list, name="movie-list"),
    path('<int:id>', movie_details, name="movie-detail")
]
