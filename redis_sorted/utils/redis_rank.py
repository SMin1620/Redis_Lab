import redis

from django.core.cache import cache

from redis_sorted.models import Movie


# class RedisRanker:
#     """레디스를 이용한 랭커"""
#     def __init__(self, conn_redis, key, is_ranker_reset=True):
#         """
#           :param conn_redis:Redis<ConnectionPool<Connection>>: 레디스연결객체
#           :param key:str: 랭커를 저장할 Redis Key
#           :param is_ranker_reset:bool: 랭커를 초기화하고 시작할지 여부
#         """
#         self.conn_redis = conn_redis
#         self.key = key
#         if is_ranker_reset is True:
#             self.conn_redis.delete(self.key)
#
#     def getScore(self, str_member):
#         """
#           멤버 점수를 조회한다
#           :param str_member:str: 조회할 멤버
#           :return score:float: 멤버 점수
#         """
#         return int(self.conn_redis.zscore(name=self.key, value=str_member) or 0)
#
#     def getRank(self, str_member):
#         """
#           멤버 랭킹을 조회한다
#           :param str_member:str: 조회할 멤버
#           :return num_rank:int: 멤버 랭킹(1위 1, 2위 2 리턴), -1 이면 랭킹 정보 없음
#         """
#         return int(self.conn_redis.zrevrank(name=self.key, value=str_member) or -2) + 1
#
#     def getTops(self, return_count=3):
#         """
#           상위 랭킹 몇 개에 대해 리턴한다
#           :param return_count:int: 리턴할 개수
#           :return tops:list: 상위에 위치한 멤버 리스트
#         """
#         return self.conn_redis.zrevrangebyscore(name=self.key, min="-inf", max="+inf", start=0, num=return_count)


def set_rank():
    movies = Movie.objects.all()
    data = {}

    for movie in movies:
        name = movie.name
        score = float(movie.score)
        ticket_count = movie.ticket_count
        if score != 0:
            data[name] = score
    return data


def create_rank(redis_conn):
    data = set_rank()
    rank_data = redis_conn.zadd('movie', data)
    return rank_data


def get_rank(redis_conn):
    rank = cache.get('movie')
    if rank is None:
        create_rank(redis_conn)
    rank_range = redis_conn.zrevrangebyscore(name='movie', min=2, max=5, withscores=True)

    return rank_range


