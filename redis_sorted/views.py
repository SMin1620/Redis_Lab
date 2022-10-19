import redis

from rest_framework import mixins, viewsets, views, status
from rest_framework.response import Response

from redis_sorted.serializers import MovieSerializer, MovieRankSerializer
from redis_sorted.models import Movie
from redis_sorted.utils.redis_rank import get_rank


redis_conn = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)


class MovieListViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRankAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        cache_data = get_rank(redis_conn)


        return Response(cache_data, status=status.HTTP_200_OK)




