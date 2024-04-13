from rest_framework import serializers
from movie_app.movie.models import Movie, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name']


class MovieSerializer(serializers.ModelSerializer):

    director = DirectorSerializer(many=False)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'genre', 'director']

    def create(self, validated_data):

        director_data = validated_data.pop('director', None)
        director, created = Director.objects.get_or_create(**director_data)

        movie_data = {
            **validated_data,
            'director': director,
        }

        return Movie.objects.create(**movie_data)
