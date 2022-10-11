import redis

from django.db import models


redis_conn = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)


class Movie(models.Model):
    name = models.CharField('영화 이름', max_length=100)
    ticket_count = models.PositiveIntegerField('예매 수')
    score = models.DecimalField('평점', max_digits=4, decimal_places=2, null=True, default=0)

    @property
    def views(self):
        return redis_conn.zscore('movie', str(self.id))

    @property
    def rank(self):
        return redis_conn.zrank('movie', str(self.id))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movie'