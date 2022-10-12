from rest_framework import serializers

from redis_sorted.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieRankSerializer(serializers.ModelSerializer):
    rank = serializers.Field()

    class Meta:
        model = Movie
        fields = [
            'rank'
        ]
