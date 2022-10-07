from django.urls import path

from redis_sorted.views import (
    MovieListViewSet,
    MovieRankAPIView
)


movie_list = MovieListViewSet.as_view({
    'get': 'list'
})


urlpatterns = [
    path('', movie_list),
    path('rank/', MovieRankAPIView.as_view()),
]
