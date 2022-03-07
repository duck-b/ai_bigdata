from rest_framework import serializers
from .models import MMovie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'movie_id',
            'movie_title',
            'movie_url',
            'movie_aud',
            'movie_net',
            'movie_rep',
            'movie_poster',
            'movie_genre',
            'movie_country',
            'movie_runtime',
            'movie_release',
            'movie_director',
            'movie_age',
            'movie_content'
        )
        model = MMovie
