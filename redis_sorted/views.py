import redis

from rest_framework import mixins, viewsets, views

from redis_sorted.serializers import MovieSerializer
from redis_sorted.models import Movie
from redis_sorted.utils.redis_rank import RedisRanker


conn_redis = redis.Redis(host='localhost', port=6379)
movieRanker = RedisRanker(conn_redis, 'movie')


class MovieListViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRankAPIView(views.APIView):
    pass


