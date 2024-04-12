
from rest_framework.response import Response
from rest_framework import generics as api_views, status

from movie_app.movie.models import Movie
from movie_app.movie_api.serializers import MovieSerializer


class MovieList(api_views.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, *args, **kwargs):

        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)
