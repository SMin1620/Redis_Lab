from rest_framework import mixins, viewsets, views

from redis_sorted.serializers import MovieSerializer
from redis_sorted.models import Movie


class MovieListViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRankAPIView(views.APIView):
    pass


