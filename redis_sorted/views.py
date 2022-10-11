import redis

from rest_framework import mixins, viewsets, views, status
from rest_framework.response import Response

from redis_sorted.serializers import MovieSerializer
from redis_sorted.models import Movie
from redis_sorted.utils.redis_rank import RedisRanker, get_score


conn_redis = redis.Redis(host='localhost', port=6379)
movieRanker = RedisRanker(conn_redis, 'movie_score')


class MovieListViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRankAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        pass

        # cache_data = get_score()
        # cache_data = movieRanker.getScore('Avengers')
        # return Response(cache_data, status=status.HTTP_200_OK)


